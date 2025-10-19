#!/usr/bin/env python3
"""
Validate Maximum Protection Licensing
Ensures comprehensive legal protection mechanisms are in place
"""

import argparse
import sys
import json
import re
from pathlib import Path


def validate_maximum_license_file(license_path):
    """Validate maximum protection LICENSE.txt contains all enhanced protections"""
    if not license_path.exists():
        return False, "LICENSE.txt not found"

    content = license_path.read_text()

    # Maximum protection specific requirements
    protection_requirements = [
        ("MAXIMUM PROTECTION v2.0", "Not maximum protection license version"),
        ("LIQUIDATED DAMAGES SCHEDULE", "Missing liquidated damages schedule"),
        ("$250,000", "Missing $250,000 AI training penalty"),
        ("$100,000", "Missing $100,000 commercial use penalty"),
        ("$500,000", "Missing $500,000 circumvention penalty"),
        ("CRIMINAL LAW NOTICE", "Missing criminal law notice section"),
        ("18 U.S.C. §1030", "Missing CFAA reference"),
        ("18 U.S.C. §1831", "Missing Economic Espionage Act reference"),
        ("17 U.S.C. §1201", "Missing DMCA reference"),
        ("PERSONAL LIABILITY", "Missing personal liability section"),
        ("Corporate veils SHALL be pierced", "Missing corporate veil piercing"),
        ("TREBLE DAMAGES", "Missing treble damages provision"),
        ("$10,000,000", "Missing punitive damages cap"),
        ("3x multiplier", "Missing attorney fee multiplier"),
        ("AUDIT RIGHTS", "Missing audit rights"),
        ("48-hour notice", "Missing forensic audit provision"),
        ("$1,000,000 bond", "Missing challenge bond requirement"),
        ("NO DEFENSE CLAUSE", "Missing no defense clause"),
        ("Fair use or research exception", "Missing fair use exclusion"),
        ("DIGITAL FINGERPRINT", "Missing digital fingerprint requirement"),
        ("forensic evidence", "Missing forensic tracking"),
        ("INTERNATIONAL ENFORCEMENT", "Missing international enforcement"),
        ("Berne Convention", "Missing Berne Convention reference"),
        ("SEVERABILITY WITH TEETH", "Missing enhanced severability"),
        ("DOUBLING of remaining", "Missing damage doubling provision"),
        ("10x all damages", "Missing major tech company multiplier"),
        ("RICO", "Missing RICO Act reference"),
        ("NO JURY TRIAL", "Missing jury trial waiver for violators"),
        ("Superior Court of California", "Missing exclusive jurisdiction"),
        ("10 years from discovery", "Missing extended limitations period")
    ]

    failed_checks = []
    for requirement, error_msg in protection_requirements:
        if requirement not in content:
            failed_checks.append(error_msg)

    if failed_checks:
        return False, f"Maximum protection requirements missing:\n  • " + "\n  • ".join(failed_checks[:5]) + \
               (f"\n  • ... and {len(failed_checks)-5} more" if len(failed_checks) > 5 else "")

    return True, "✓ All maximum protection license provisions present"


def validate_forensic_metadata(skill_path):
    """Validate forensic metadata file exists and is properly formatted"""
    metadata_path = skill_path / ".forensic_metadata.json"

    if not metadata_path.exists():
        return False, "Missing .forensic_metadata.json forensic tracking file"

    try:
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)

        # Check required fields
        required_fields = [
            "license_version",
            "entity",
            "digital_signature",
            "blockchain_marker",
            "forensic_tracking",
            "enforcement"
        ]

        missing_fields = [field for field in required_fields if field not in metadata]
        if missing_fields:
            return False, f"Forensic metadata missing fields: {', '.join(missing_fields)}"

        # Validate license version
        if "MAXIMUM-PROTECTION" not in metadata.get("license_version", ""):
            return False, "Forensic metadata not tagged as maximum protection"

        # Validate enforcement structure
        enforcement = metadata.get("enforcement", {})
        if "liquidated_damages" not in enforcement:
            return False, "Missing liquidated damages in forensic metadata"

        damages = enforcement.get("liquidated_damages", {})
        if damages.get("ai_training") != 250000:
            return False, "Incorrect AI training damage amount in metadata"

        return True, "✓ Forensic metadata properly configured"

    except json.JSONDecodeError:
        return False, "Invalid JSON in forensic metadata file"
    except Exception as e:
        return False, f"Error reading forensic metadata: {str(e)}"


def validate_criminal_provisions(license_path):
    """Validate comprehensive criminal law provisions"""
    if not license_path.exists():
        return False, "Cannot validate criminal provisions - LICENSE.txt not found"

    content = license_path.read_text()

    criminal_statutes = [
        ("18 U.S.C. §1030", "Computer Fraud and Abuse Act"),
        ("18 U.S.C. §1831", "Economic Espionage Act"),
        ("17 U.S.C. §1201", "DMCA anti-circumvention"),
        ("18 U.S.C. §1343", "Wire Fraud"),
        ("18 U.S.C. §1961", "RICO Act"),
        ("Cal. Penal Code §502", "California computer crimes")
    ]

    missing_statutes = []
    for statute, name in criminal_statutes:
        if statute not in content:
            missing_statutes.append(f"{statute} ({name})")

    if missing_statutes:
        return False, f"Missing criminal statutes: {', '.join(missing_statutes)}"

    # Check for criminal prosecution commitment
    if "WILL seek criminal prosecution" not in content:
        return False, "Missing affirmative criminal prosecution commitment"

    return True, "✓ All criminal law provisions present"


def validate_liquidated_damages(license_path):
    """Validate complete liquidated damages schedule"""
    if not license_path.exists():
        return False, "Cannot validate damages - LICENSE.txt not found"

    content = license_path.read_text()

    damage_schedule = {
        "AI/ML Training": ("$250,000", 250000),
        "Commercial Use": ("$100,000", 100000),
        "Redistribution": ("$50,000", 50000),
        "Modification": ("$75,000", 75000),
        "Reverse Engineering": ("$150,000", 150000),
        "Circumvention": ("$500,000", 500000),
        "Continuing": ("$10,000 per day", 10000),
        "Major Tech": ("$2.5M", 2500000)
    }

    issues = []
    for violation_type, (amount_str, amount_int) in damage_schedule.items():
        if amount_str not in content:
            issues.append(f"{violation_type}: {amount_str}")

    if issues:
        return False, f"Incomplete damage schedule: {', '.join(issues)}"

    # Check for damage multipliers
    if "TRIPLE all damages" not in content:
        return False, "Missing willful violation tripling provision"

    if "10x all damages" not in content:
        return False, "Missing major tech company 10x multiplier"

    return True, "✓ Complete liquidated damages schedule"


def validate_enforcement_mechanisms(license_path):
    """Validate all enforcement mechanisms are present"""
    if not license_path.exists():
        return False, "Cannot validate enforcement - LICENSE.txt not found"

    content = license_path.read_text()

    enforcement_features = [
        ("IMMEDIATE INJUNCTIVE RELIEF", "immediate injunction"),
        ("without bond", "bond waiver for injunctions"),
        ("PUNITIVE DAMAGES", "punitive damages"),
        ("3x multiplier", "attorney fee multiplier"),
        ("DISGORGEMENT", "profit disgorgement"),
        ("PUBLIC DISCLOSURE", "public disclosure remedy"),
        ("DESTRUCTION of all copies", "destruction remedy"),
        ("forensic examination", "forensic audit rights"),
        ("48-hour notice", "audit notice period"),
        ("$1,000,000 bond", "challenge bond requirement")
    ]

    missing = []
    for feature, description in enforcement_features:
        if feature not in content:
            missing.append(description)

    if missing:
        return False, f"Missing enforcement mechanisms: {', '.join(missing[:3])}" + \
                     (f" (+{len(missing)-3} more)" if len(missing) > 3 else "")

    return True, "✓ All enforcement mechanisms present"


def validate_maximum_protection_skill(skill_path):
    """Comprehensive validation of maximum protection licensing"""
    skill_path = Path(skill_path).resolve()

    if not skill_path.exists():
        return False, f"Skill directory not found: {skill_path}"

    if not skill_path.is_dir():
        return False, f"Path is not a directory: {skill_path}"

    print(f"🛡️ VALIDATING MAXIMUM PROTECTION: {skill_path.name}")
    print("=" * 60)

    all_valid = True
    results = []

    # 1. Validate maximum protection license file
    license_path = skill_path / "LICENSE.txt"
    valid, message = validate_maximum_license_file(license_path)
    status = "✅" if valid else "❌"
    results.append(f"{status} License File: {message}")
    all_valid = all_valid and valid

    # 2. Validate forensic metadata
    valid, message = validate_forensic_metadata(skill_path)
    status = "✅" if valid else "❌"
    results.append(f"{status} Forensic Metadata: {message}")
    all_valid = all_valid and valid

    # 3. Validate criminal provisions
    if license_path.exists():
        valid, message = validate_criminal_provisions(license_path)
        status = "✅" if valid else "❌"
        results.append(f"{status} Criminal Provisions: {message}")
        all_valid = all_valid and valid

    # 4. Validate liquidated damages
    if license_path.exists():
        valid, message = validate_liquidated_damages(license_path)
        status = "✅" if valid else "❌"
        results.append(f"{status} Liquidated Damages: {message}")
        all_valid = all_valid and valid

    # 5. Validate enforcement mechanisms
    if license_path.exists():
        valid, message = validate_enforcement_mechanisms(license_path)
        status = "✅" if valid else "❌"
        results.append(f"{status} Enforcement: {message}")
        all_valid = all_valid and valid

    # 6. Check for SKILL.md maximum protection reference
    skill_md_path = skill_path / "SKILL.md"
    if skill_md_path.exists():
        content = skill_md_path.read_text()
        if "MAXIMUM PROTECTION" in content:
            results.append("✅ SKILL.md: Maximum protection reference found")
        else:
            results.append("❌ SKILL.md: Missing maximum protection reference")
            all_valid = False

    # Print results
    for result in results:
        print(result)

    print("=" * 60)
    if all_valid:
        print("🛡️ MAXIMUM PROTECTION VERIFIED!")
        print("\n⚠️ ACTIVE PROTECTION FEATURES:")
        print("  • $250,000 liquidated damages for AI training")
        print("  • Criminal prosecution under CFAA, DMCA, Economic Espionage Act")
        print("  • Personal liability with corporate veil piercing")
        print("  • 10x damages for major tech companies (>$1B market cap)")
        print("  • Forensic tracking and digital watermarking")
        print("  • 48-hour notice audit rights")
        print("  • No valid defenses (fair use excluded)")
        print("  • International enforcement under Berne/TRIPS")
    else:
        print("❌ MAXIMUM PROTECTION VALIDATION FAILED")
        print("   Review and address the issues above for maximum protection")

    return all_valid


def main():
    parser = argparse.ArgumentParser(
        description="Validate maximum protection licensing with comprehensive legal safeguards"
    )
    parser.add_argument(
        "--skill-path",
        required=True,
        help="Path to the skill directory to validate"
    )

    args = parser.parse_args()

    valid = validate_maximum_protection_skill(args.skill_path)
    sys.exit(0 if valid else 1)


if __name__ == "__main__":
    main()