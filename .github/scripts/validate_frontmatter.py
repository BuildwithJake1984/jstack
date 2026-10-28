#!/usr/bin/env python3
"""Validate YAML frontmatter for JStack write-ups."""

from __future__ import annotations

import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]

FRONTMATTER_RE = re.compile(r"^(?:\s*\n)?---\r?\n(.*?)\r?\n---", re.DOTALL)


def has_frontmatter_fence(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if not line.strip():
            continue
        return line.strip() == "---"
    return False


def extract_frontmatter(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    return match.group(1)


def gh_error(path: Path, message: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    print(f"::error file={rel}::{message}")


def require_str(data: dict, key: str, path: Path, errors: list[str]) -> None:
    value = data.get(key)
    if value is None:
        errors.append(f"Missing {key}")
        return
    if isinstance(value, (date, datetime)):
        return
    if not isinstance(value, str) or not value.strip():
        errors.append(f"Missing or empty {key}")


def require_tags(data: dict, path: Path, errors: list[str]) -> None:
    if "tags" not in data:
        errors.append("Missing tags")


def check_lesson(data: dict, path: Path, errors: list[str]) -> None:
    if data.get("type") != "lesson":
        errors.append("type must be lesson")
    require_str(data, "title", path, errors)
    require_str(data, "slug", path, errors)
    require_str(data, "date", path, errors)
    require_str(data, "status", path, errors)
    require_tags(data, path, errors)
    require_str(data, "purpose", path, errors)
    if data.get("status") == "draft":
        errors.append("Lessons must not use status: draft")


def check_tool(data: dict, path: Path, errors: list[str]) -> None:
    if data.get("type") != "tool":
        errors.append("type must be tool")
    require_str(data, "title", path, errors)
    require_tags(data, path, errors)
    require_str(data, "purpose", path, errors)


def check_skill(data: dict, path: Path, errors: list[str]) -> None:
    if data.get("type") != "skill":
        errors.append("type must be skill")
    require_str(data, "name", path, errors)
    require_str(data, "description", path, errors)
    require_tags(data, path, errors)
    require_str(data, "purpose", path, errors)


def check_reference(data: dict, path: Path, errors: list[str]) -> None:
    if data.get("type") != "reference":
        errors.append("type must be reference")
    require_str(data, "title", path, errors)
    require_tags(data, path, errors)
    require_str(data, "purpose", path, errors)


def require_source_urls(data: dict, errors: list[str]) -> None:
    sources = data.get("sources")
    if sources is None:
        errors.append("Missing sources")
        return
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty list")
        return
    for index, item in enumerate(sources):
        if isinstance(item, str):
            if not item.strip():
                errors.append(f"sources[{index}] must be a non-empty URL")
            continue
        if isinstance(item, dict):
            url = item.get("url")
            if not isinstance(url, str) or not url.strip():
                errors.append(f"sources[{index}] must include url")
            continue
        errors.append(f"sources[{index}] must be a URL string or mapping with url")


def check_news_insights(data: dict, path: Path, errors: list[str]) -> None:
    if data.get("type") != "news-insights":
        errors.append("type must be news-insights")
    require_str(data, "title", path, errors)
    require_str(data, "date", path, errors)
    require_str(data, "week_of", path, errors)
    require_str(data, "status", path, errors)
    require_tags(data, path, errors)
    require_str(data, "purpose", path, errors)
    status = data.get("status")
    if status not in ("draft", "published"):
        errors.append("status must be draft or published")
    require_source_urls(data, errors)


def iter_lessons() -> list[Path]:
    paths: list[Path] = []
    for base in (
        "insights/ai-agents",
        "insights/design",
        "insights/development",
        "insights/marketing",
    ):
        for path in sorted((ROOT / base).glob("*.md")):
            if path.name == "README.md":
                continue
            paths.append(path)
    return paths


def iter_tools() -> list[Path]:
    paths: list[Path] = []
    for base in (
        "libraries/tools/design",
        "libraries/tools/ai-agents",
        "libraries/tools/development",
        "libraries/tools/marketing",
    ):
        folder = ROOT / base
        if not folder.is_dir():
            continue
        paths.extend(
            p for p in sorted(folder.glob("*.md")) if p.name != "README.md"
        )
    return paths


def iter_skills() -> list[Path]:
    paths: list[Path] = []
    for base in ("personal-workflows", "business-workflows"):
        root = ROOT / base
        for path in sorted(root.glob("**/skills/*.md")):
            if path.name == "README.md":
                continue
            paths.append(path)
        paths.extend(sorted(root.glob("**/skills/*/SKILL.md")))
    return paths


def iter_references() -> list[Path]:
    return sorted(
        p
        for p in (ROOT / "libraries/ui-libraries").glob("*.md")
        if p.name != "README.md"
    )


def iter_templates() -> list[Path]:
    paths: list[Path] = []
    for base in (
        "libraries/templates/ai-agents",
        "libraries/templates/design",
        "libraries/templates/development",
        "libraries/templates/marketing",
    ):
        root = ROOT / base
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*.md")):
            if path.name == "README.md" and path.parent == root:
                continue
            paths.append(path)
    return paths


def iter_updates() -> list[Path]:
    updates = ROOT / "updates"
    if not updates.is_dir():
        return []
    return sorted(p for p in updates.glob("*.md") if p.name != "README.md")


def iter_news_insights() -> list[Path]:
    folder = ROOT / "insights/news-and-insights"
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.glob("*.md") if p.name != "README.md")


def validate_file(path: Path, schema_check) -> bool:
    rel = path.relative_to(ROOT)
    print(f"Checking {rel}")

    if not has_frontmatter_fence(path):
        gh_error(path, "Missing opening frontmatter fence")
        return False

    block = extract_frontmatter(path)
    if block is None:
        gh_error(path, "Could not extract frontmatter block")
        return False

    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError as exc:
        gh_error(path, f"Invalid YAML frontmatter: {exc}")
        return False

    if data is None:
        gh_error(path, "Frontmatter is empty")
        return False
    if not isinstance(data, dict):
        gh_error(path, "Frontmatter must be a YAML mapping")
        return False

    errors: list[str] = []
    schema_check(data, path, errors)
    for message in errors:
        gh_error(path, message)
    return not errors


def validate_yaml_only(path: Path) -> bool:
    """Parse frontmatter as YAML when the file has a fence; skip files without one."""
    if not has_frontmatter_fence(path):
        return True

    rel = path.relative_to(ROOT)
    print(f"Checking YAML {rel}")
    block = extract_frontmatter(path)
    if block is None:
        gh_error(path, "Could not extract frontmatter block")
        return False

    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError as exc:
        gh_error(path, f"Invalid YAML frontmatter: {exc}")
        return False

    if data is None:
        gh_error(path, "Frontmatter is empty")
        return False
    if not isinstance(data, dict):
        gh_error(path, "Frontmatter must be a YAML mapping")
        return False
    return True


def main() -> int:
    ok = True

    for path in iter_lessons():
        ok = validate_file(path, check_lesson) and ok
    for path in iter_tools():
        ok = validate_file(path, check_tool) and ok
    for path in iter_skills():
        ok = validate_file(path, check_skill) and ok
    for path in iter_references():
        ok = validate_file(path, check_reference) and ok
    for path in iter_templates():
        ok = validate_yaml_only(path) and ok
    for path in iter_updates():
        ok = validate_yaml_only(path) and ok
    for path in iter_news_insights():
        ok = validate_file(path, check_news_insights) and ok

    if ok:
        print("Write-up frontmatter OK.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
