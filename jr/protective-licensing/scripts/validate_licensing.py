#!/usr/bin/env python3
"""
Validate Protective Licensing
Ensures skills have proper protective licensing applied
"""

import argparse
import sys
from pathlib import Path
import re


def validate_license_file(license_path):
    """Validate that LICENSE.txt contains required elements"""
    if not license_path.exists():
        return False, "LICENSE.txt not found"

    content = license_path.read_text()

    # Check for essential components
    required_elements = [
        ("AI/ML TRAINING PROHIBITION", "Missing AI/ML training prohibition section"),
        ("SHALL NOT be used", "Missing explicit prohibition language"),
        ("training data for any artificial intelligence", "Missing AI training prohibition"),
        ("COMMERCIAL USE RESTRICTION", "Missing commercial use restriction"),
        ("REDISTRIBUTION RESTRICTION", "Missing redistribution restriction"),
        ("Copyright (c)", "Missing copyright notice"),
        ("All rights reserved", "Missing rights reservation"),
        ("LICENSE VIOLATIONS", "Missing violation consequences section"),
        ("GOVERNING LAW", "Missing governing law section")
    ]

    for element, error_msg in required_elements:
        if element not in content:
            return False, error_msg

    return True, "LICENSE.txt is properly formatted"


def validate_skill_md(skill_md_path):
    """Validate that SKILL.md references the license"""
    if not skill_md_path.exists():
        return False, "SKILL.md not found"

    content = skill_md_path.read_text()

    # Check for frontmatter
    if not content.startswith("---"):
        return False, "SKILL.md missing YAML frontmatter"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter = match.group(1)

    # Check for license reference
    if "license:" not in frontmatter:
        return False, "SKILL.md missing license field in frontmatter"

    if "LICENSE.txt" not in frontmatter:
        return False, "SKILL.md license field doesn't reference LICENSE.txt"

    return True, "SKILL.md properly references license"


def validate_ai_prohibition(license_path):
    """Validate comprehensive AI training prohibition"""
    if not license_path.exists():
        return False, "Cannot validate AI prohibition - LICENSE.txt not found"

    content = license_path.read_text()

    ai_prohibitions = [
        "training data",
        "machine learning",
        "large language model",
        "fine-tuning",
        "embeddings",
        "vector representations",
        "retrieval-augmented generation",
        "RAG",
        "data mining",
        "synthetic data generation"
    ]

    missing = []
    for term in ai_prohibitions:
        if term.lower() not in content.lower():
            missing.append(term)

    if missing:
        return False, f"AI prohibition incomplete. Missing terms: {', '.join(missing)}"

    return True, "Comprehensive AI training prohibition found"


def validate_entity_info(license_path):
    """Validate that entity information is complete"""
    if not license_path.exists():
        return False, "Cannot validate entity info - LICENSE.txt not found"

    content = license_path.read_text()

    # Check for placeholder text
    placeholders = [
        "[YOUR NAME",
        "[Contact information to be provided]",
        "[YOUR EMAIL",
        "[YOUR JURISDICTION"
    ]

    found_placeholders = []
    for placeholder in placeholders:
        if placeholder in content:
            found_placeholders.append(placeholder)

    if found_placeholders:
        return False, f"License contains placeholders: {', '.join(found_placeholders)}"

    # Check for actual entity information
    if "Copyright (c)" not in content:
        return False, "Missing copyright statement"

    # Extract copyright line
    copyright_match = re.search(r'Copyright \(c\) \d{4} (.+)', content)
    if not copyright_match:
        return False, "Invalid copyright format"

    entity = copyright_match.group(1).strip()
    if len(entity) < 3:
        return False, "Entity name appears incomplete"

    return True, f"Entity information complete: {entity}"


def validate_skill_licensing(skill_path):
    """Comprehensive validation of skill licensing"""
    skill_path = Path(skill_path).resolve()

    if not skill_path.exists():
        return False, f"Skill directory not found: {skill_path}"

    if not skill_path.is_dir():
        return False, f"Path is not a directory: {skill_path}"

    print(f"🔍 Validating protective licensing for: {skill_path.name}")
    print("-" * 50)

    all_valid = True
    results = []

    # 1. Validate LICENSE.txt exists and is formatted correctly
    license_path = skill_path / "LICENSE.txt"
    valid, message = validate_license_file(license_path)
    status = "✅" if valid else "❌"
    results.append(f"{status} LICENSE.txt: {message}")
    all_valid = all_valid and valid

    # 2. Validate SKILL.md references license
    skill_md_path = skill_path / "SKILL.md"
    valid, message = validate_skill_md(skill_md_path)
    status = "✅" if valid else "❌"
    results.append(f"{status} SKILL.md: {message}")
    all_valid = all_valid and valid

    # 3. Validate AI prohibition is comprehensive
    if license_path.exists():
        valid, message = validate_ai_prohibition(license_path)
        status = "✅" if valid else "❌"
        results.append(f"{status} AI Prohibition: {message}")
        all_valid = all_valid and valid

    # 4. Validate entity information is complete
    if license_path.exists():
        valid, message = validate_entity_info(license_path)
        status = "✅" if valid else "❌"
        results.append(f"{status} Entity Info: {message}")
        all_valid = all_valid and valid

    # Print results
    for result in results:
        print(result)

    print("-" * 50)
    if all_valid:
        print("✅ All licensing validations passed!")
    else:
        print("❌ Some validations failed. Please address the issues above.")

    return all_valid


def main():
    parser = argparse.ArgumentParser(
        description="Validate protective licensing application"
    )
    parser.add_argument(
        "--skill-path",
        required=True,
        help="Path to the skill directory to validate"
    )

    args = parser.parse_args()

    valid = validate_skill_licensing(args.skill_path)
    sys.exit(0 if valid else 1)


if __name__ == "__main__":
    main()