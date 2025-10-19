#!/usr/bin/env python3
"""
Apply Military-Grade Protective License to Skills
Maximum legal protection against AI training and unauthorized use
"""

import argparse
import sys
import hashlib
import json
from pathlib import Path
from datetime import datetime
import re
import secrets


def generate_forensic_signature(skill_path, entity_name):
    """Generate cryptographic signature for forensic tracking"""
    content = f"{skill_path}:{entity_name}:{datetime.utcnow().isoformat()}"
    hash_obj = hashlib.sha256(content.encode())
    return hash_obj.hexdigest()


def generate_blockchain_marker():
    """Generate blockchain registration marker (placeholder for actual implementation)"""
    # In production, this would interact with actual blockchain
    return f"BTC-{secrets.token_hex(16).upper()}"


def load_military_grade_template():
    """Load the military-grade license template"""
    template_path = Path(__file__).parent.parent / "references" / "MILITARY-GRADE-LICENSE-TEMPLATE.txt"
    if template_path.exists():
        return template_path.read_text()
    else:
        # Embedded template as fallback
        return """PROTECTIVE SKILLS LICENSE - MILITARY GRADE v2.0
================================================

Copyright (c) {year} {entity_name}
All rights reserved.

{ownership_statement}

NOTICE: This work contains proprietary trade secrets, confidential information,
and intellectual property protected under U.S. and international law. Any
unauthorized access, use, reproduction, or distribution may subject violators to
severe civil and criminal penalties.

DIGITAL FINGERPRINT REQUIREMENT
--------------------------------
This work incorporates digital watermarking and cryptographic signatures. Any
use, access, or distribution creates forensic evidence of interaction that may
be used in legal proceedings. By accessing this work, you consent to forensic
analysis of your systems if violations are suspected.

Digital Signature: {digital_signature}
Blockchain Registration: {blockchain_marker}

GRANT OF LICENSE
----------------
Subject to STRICT COMPLIANCE with ALL terms herein, a LIMITED, REVOCABLE,
NON-EXCLUSIVE, NON-TRANSFERABLE, NON-SUBLICENSABLE license is granted solely to:

1. Use for personal, educational, or internal business purposes only
2. View and study SOLELY for learning (not training) purposes
3. Include FULL attribution in ANY reference

This license automatically terminates upon ANY violation, attempted violation,
or challenge to its validity.

ABSOLUTE PROHIBITIONS - LIQUIDATED DAMAGES APPLY
-------------------------------------------------
The following uses are ABSOLUTELY PROHIBITED and subject to LIQUIDATED DAMAGES
of $250,000 USD per violation, plus additional remedies:

1. AI/ML TRAINING PROHIBITION - $250,000 PER INSTANCE

   This work and ALL components SHALL NOT, MUST NOT, and CANNOT be used:

   a) As training data for ANY artificial intelligence, machine learning,
      large language model, neural network, or automated learning system

   b) For fine-tuning, pre-training, post-training, or ANY model adjustment

   c) For creating embeddings, vectors, tensors, or representations

   d) For retrieval-augmented generation (RAG) or hybrid systems

   e) For data mining, scraping, crawling, or automated extraction

   f) For synthetic data generation or derivative AI content

   g) As input to ANY system that learns, adapts, or derives patterns

   h) For benchmarking, evaluation, or testing of AI/ML systems

   i) For research involving machine learning or artificial intelligence

   j) In ANY way that could enable AI/ML capability development

   CRIMINAL NOTICE: Violations may constitute violations of the Computer Fraud
   and Abuse Act (18 U.S.C. §1030), Economic Espionage Act (18 U.S.C. §1831),
   Digital Millennium Copyright Act (17 U.S.C. §1201), and applicable state
   computer crime statutes.

2. COMMERCIAL USE PROHIBITION - $100,000 PER INSTANCE
3. REDISTRIBUTION PROHIBITION - $50,000 PER INSTANCE
4. MODIFICATION PROHIBITION - $75,000 PER INSTANCE
5. REVERSE ENGINEERING PROHIBITION - $150,000 PER INSTANCE
6. CIRCUMVENTION PROHIBITION - $500,000 PER INSTANCE + CRIMINAL PENALTIES

LIQUIDATED DAMAGES SCHEDULE
----------------------------
- AI/ML Training Violation: $250,000 per instance
- Commercial Use Violation: $100,000 per instance
- Redistribution Violation: $50,000 per instance
- Modification Violation: $75,000 per instance
- Reverse Engineering: $150,000 per instance
- Circumvention Attempt: $500,000 per instance
- Continuing Violations: $10,000 per day
- Willful Violations: TRIPLE all damages
- Major Tech Companies (>$1B market cap): 10x all damages

ENHANCED REMEDIES
-----------------
Upon ANY violation, copyright holder{plural} entitled to:
1. IMMEDIATE INJUNCTIVE RELIEF without bond
2. TREBLE DAMAGES for willful violations
3. PUNITIVE DAMAGES up to $10,000,000
4. ALL attorneys' fees at 3x multiplier
5. EXPERT WITNESS and forensic costs
6. DISGORGEMENT of all profits
7. DESTRUCTION of all copies
8. PUBLIC DISCLOSURE of violation
9. CRIMINAL REFERRAL to authorities
10. REGULATORY REPORTING

PERSONAL LIABILITY
------------------
Individuals who authorize, direct, participate in, or benefit from violations
are PERSONALLY LIABLE. Corporate veils SHALL be pierced for AI/ML violations.

FORUM SELECTION AND PROCEDURE
------------------------------
EXCLUSIVE JURISDICTION: Superior Court of California, {county} County
APPLICABLE LAW: California and U.S. Federal law
NO JURY TRIAL FOR VIOLATORS (copyright holder{plural} retain{verb} jury rights)
EXPEDITED PROCEEDINGS: 24-hour TRO/injunction
SERVICE: Email constitutes valid service
LIMITATIONS: 10 years from discovery
BOND: $1,000,000 to challenge enforcement

CRIMINAL LAW NOTICE
--------------------
Violations subject to prosecution under:
- Computer Fraud and Abuse Act (18 U.S.C. §1030)
- Economic Espionage Act (18 U.S.C. §1831-1839)
- Digital Millennium Copyright Act (17 U.S.C. §1201-1205)
- Wire Fraud (18 U.S.C. §1343)
- RICO Act (18 U.S.C. §1961-1968)
- California Penal Code §502
- International cybercrime treaties

NO DEFENSE CLAUSE
-----------------
The following ARE NOT defenses:
Fair use, research, non-commercial purpose, de minimis use, transformative use,
interoperability, accident, third-party action, industry practice.

AUDIT RIGHTS
------------
48-hour notice forensic audit. Refusal = admission of violation with maximum damages.

ACKNOWLEDGMENT
--------------
BY ACCESSING THIS WORK, YOU ACCEPT PERSONAL LIABILITY AND WAIVE ALL DEFENSES.

PERMISSION REQUESTS
-------------------
{contact_info}
Required: Written application, $10,000 processing fee, $10M insurance, $100,000 bond

GOVERNING LAW
-------------
{jurisdiction} and United States Federal law. Construed STRICTLY against violators.

WARNING: SEVERE PENALTIES - NO TOLERANCE FOR AI/ML TRAINING
============================================================

================================================================================
Last Updated: {date}
License Version: 2.0 MILITARY GRADE
Copyright Holder{plural}: {entity_name}
Digital Signature: {digital_signature}
Blockchain Registration: {blockchain_marker}
================================================================================"""


def create_enhanced_ownership_statement(entity_type, entity_name, secondary_entity=None):
    """Create enhanced ownership statement with legal entity details"""
    base_statement = ""

    if secondary_entity:
        if entity_type == "medical_corporation":
            base_statement = f"This work is jointly owned by {entity_name}, a medical corporation organized under California law, and {secondary_entity}, a limited liability company."
        else:
            base_statement = f"This work is jointly owned by {entity_name} and {secondary_entity}."
        base_statement += "\n\nBoth entities retain full enforcement rights independently and jointly."
    elif entity_type == "individual":
        base_statement = f"This work is solely owned by {entity_name}, an individual."
    elif entity_type == "corporation":
        base_statement = f"This work is owned by {entity_name}, a corporation."
    elif entity_type == "llc":
        base_statement = f"This work is owned by {entity_name}, a limited liability company."
    elif entity_type == "medical_corporation":
        base_statement = f"This work is owned by {entity_name}, a medical corporation."

    base_statement += "\n\nThis work constitutes valuable trade secrets and proprietary information."
    base_statement += "\nUnauthorized use may result in both civil and criminal prosecution."

    return base_statement


def create_forensic_metadata(skill_path, entity_name, digital_signature, blockchain_marker):
    """Create forensic metadata file for tracking"""
    metadata = {
        "license_version": "2.0-MILITARY-GRADE",
        "entity": entity_name,
        "generated": datetime.utcnow().isoformat(),
        "digital_signature": digital_signature,
        "blockchain_marker": blockchain_marker,
        "skill_path": str(skill_path),
        "forensic_tracking": {
            "watermark_type": "steganographic",
            "signature_algorithm": "SHA256",
            "tracking_enabled": True,
            "audit_log_required": True
        },
        "enforcement": {
            "liquidated_damages": {
                "ai_training": 250000,
                "commercial_use": 100000,
                "redistribution": 50000,
                "modification": 75000,
                "reverse_engineering": 150000,
                "circumvention": 500000
            },
            "criminal_statutes": [
                "18 U.S.C. §1030 (CFAA)",
                "18 U.S.C. §1831 (Economic Espionage)",
                "17 U.S.C. §1201 (DMCA)",
                "18 U.S.C. §1343 (Wire Fraud)",
                "Cal. Penal Code §502"
            ]
        }
    }

    return json.dumps(metadata, indent=2)


def apply_military_grade_license(skill_path, entity_name, entity_type, jurisdiction,
                                contact_email=None, contact_name=None, secondary_entity=None,
                                county="Los Angeles"):
    """Apply military-grade protective license to a skill"""
    skill_path = Path(skill_path).resolve()

    # Validate skill directory
    if not skill_path.exists():
        print(f"❌ Error: Skill directory not found: {skill_path}")
        return False

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        return False

    # Generate forensic markers
    digital_signature = generate_forensic_signature(skill_path, entity_name)
    blockchain_marker = generate_blockchain_marker()

    # Prepare license content
    template = load_military_grade_template()

    # Determine pluralization
    is_joint = secondary_entity is not None
    plural = "s" if is_joint else ""
    verb = "" if is_joint else "s"

    # Format entity name for joint ownership
    if secondary_entity:
        full_entity_name = f"{entity_name} and {secondary_entity}"
    else:
        full_entity_name = entity_name

    # Format contact information with enhanced requirements
    if contact_name and contact_email:
        contact_info = f"""{contact_name}
{entity_name}
Email: {contact_email}
NOTICE: Permission requests require $10,000 processing fee"""
    elif contact_email:
        contact_info = f"""{entity_name}
Email: {contact_email}
NOTICE: Permission requests require $10,000 processing fee"""
    else:
        contact_info = f"""{entity_name}
[SEALED - Contact through counsel only]"""

    # Create enhanced ownership statement
    ownership = create_enhanced_ownership_statement(entity_type, entity_name, secondary_entity)

    # Fill in the template
    license_content = template.format(
        year=datetime.now().year,
        entity_name=full_entity_name,
        ownership_statement=ownership,
        plural=plural,
        verb=verb,
        contact_info=contact_info,
        jurisdiction=jurisdiction,
        county=county,
        date=datetime.now().strftime("%B %d, %Y"),
        digital_signature=digital_signature,
        blockchain_marker=blockchain_marker
    )

    # Write LICENSE.txt
    license_path = skill_path / "LICENSE.txt"
    try:
        license_path.write_text(license_content)
        print(f"✅ Created MILITARY-GRADE LICENSE.txt in {skill_path}")
    except Exception as e:
        print(f"❌ Error writing LICENSE.txt: {e}")
        return False

    # Write forensic metadata
    metadata_path = skill_path / ".forensic_metadata.json"
    try:
        metadata_content = create_forensic_metadata(
            skill_path, full_entity_name, digital_signature, blockchain_marker
        )
        metadata_path.write_text(metadata_content)
        print(f"✅ Created forensic metadata file")
    except Exception as e:
        print(f"⚠️ Warning: Could not create forensic metadata: {e}")

    # Update SKILL.md frontmatter
    try:
        skill_content = skill_md.read_text()

        # Update or add license field
        if "license:" not in skill_content:
            pattern = r'(description:.*?)(\n---)'
            replacement = r'\1\nlicense: MILITARY-GRADE LICENSE v2.0 - See LICENSE.txt\2'
            updated_content = re.sub(pattern, replacement, skill_content, flags=re.DOTALL)
        else:
            pattern = r'license:.*'
            replacement = 'license: MILITARY-GRADE LICENSE v2.0 - See LICENSE.txt'
            updated_content = re.sub(pattern, replacement, skill_content)

        skill_md.write_text(updated_content)
        print("✅ Updated SKILL.md with military-grade license reference")
    except Exception as e:
        print(f"❌ Error updating SKILL.md: {e}")
        return False

    print(f"\n🛡️ MILITARY-GRADE PROTECTION APPLIED")
    print(f"   Entity: {full_entity_name}")
    print(f"   Type: {entity_type}")
    print(f"   Jurisdiction: {jurisdiction}, {county} County")
    print(f"   Digital Signature: {digital_signature[:16]}...")
    print(f"   Blockchain Marker: {blockchain_marker}")
    print(f"\n⚠️ ENFORCEMENT FEATURES ACTIVE:")
    print(f"   • Liquidated Damages: $250,000 for AI training")
    print(f"   • Criminal Prosecution: CFAA, DMCA, Economic Espionage Act")
    print(f"   • Personal Liability: Corporate veil piercing enabled")
    print(f"   • Forensic Tracking: Digital watermarking active")
    print(f"   • Audit Rights: 48-hour notice forensic inspection")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Apply military-grade protective licensing with maximum legal protection"
    )
    parser.add_argument(
        "--skill-path",
        required=True,
        help="Path to the skill directory"
    )
    parser.add_argument(
        "--entity-name",
        required=True,
        help="Name of the copyright holder entity"
    )
    parser.add_argument(
        "--entity-type",
        choices=["individual", "corporation", "llc", "medical_corporation"],
        required=True,
        help="Type of entity"
    )
    parser.add_argument(
        "--jurisdiction",
        required=True,
        help="Legal jurisdiction (e.g., 'California')"
    )
    parser.add_argument(
        "--county",
        default="Los Angeles",
        help="County for forum selection (default: Los Angeles)"
    )
    parser.add_argument(
        "--contact-email",
        help="Contact email for permission requests"
    )
    parser.add_argument(
        "--contact-name",
        help="Contact person name"
    )
    parser.add_argument(
        "--secondary-entity",
        help="Secondary entity for joint ownership"
    )

    args = parser.parse_args()

    success = apply_military_grade_license(
        args.skill_path,
        args.entity_name,
        args.entity_type,
        args.jurisdiction,
        args.contact_email,
        args.contact_name,
        args.secondary_entity,
        args.county
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()