#!/usr/bin/env python3
"""
Apply Protective License to Skills
Automates the application of the Protective Skills License to new skills
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime
import re


def load_license_template():
    """Load the protective license template"""
    template = """PROTECTIVE SKILLS LICENSE v1.0
================================

Copyright (c) {year} {entity_name}
All rights reserved.

{ownership_statement}

GRANT OF LICENSE
----------------
Subject to the terms and conditions below, you are granted a limited,
non-exclusive, non-transferable license to:

1. Use this skill for personal, educational, or internal business purposes
2. View and study the skill's code and documentation for learning purposes
3. Include attribution when referencing or discussing this skill

EXPLICIT PROHIBITIONS
---------------------
The following uses are STRICTLY PROHIBITED without prior written permission:

1. AI/ML TRAINING PROHIBITION
   This skill and all its components (including but not limited to: instruction
   text, code, scripts, documentation, examples, and metadata) SHALL NOT be used:

   a) As training data for any artificial intelligence system, machine learning
      model, large language model (LLM), neural network, or other automated
      learning system

   b) For fine-tuning, pre-training, or post-training of AI/ML models

   c) For creating embeddings, vector representations, or knowledge bases used
      in AI systems

   d) For retrieval-augmented generation (RAG) systems or similar AI-assisted
      retrieval systems

   e) For data mining, web scraping, or automated extraction for AI purposes

   f) For any form of synthetic data generation or AI-assisted derivative works

   g) As input to any automated system that generates, modifies, or derives
      content based on analysis of this work

2. COMMERCIAL USE RESTRICTION
   You may NOT use, sell, license, or commercialize this skill or derivative
   works without explicit written permission from the copyright holder{plural}.

3. REDISTRIBUTION RESTRICTION
   You may NOT redistribute, publish, or make this skill available through
   public repositories, marketplaces, or platforms without explicit written
   permission from the copyright holder{plural}.

4. MODIFICATION RESTRICTION
   You may NOT create derivative works, modifications, or adaptations of this
   skill without explicit written permission from the copyright holder{plural}.

ATTRIBUTION REQUIREMENTS
-------------------------
When referencing this skill in documentation, publications, or communications:

1. Clearly identify the copyright holder{plural}: "{entity_name}"
2. Include a link to the original source if available
3. Indicate if any modifications were made (if permitted under separate agreement)
4. Preserve all copyright and license notices

DISCLAIMER OF WARRANTIES
------------------------
THIS SKILL IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE, AND NONINFRINGEMENT.

IN NO EVENT SHALL THE COPYRIGHT HOLDER{PLURAL} BE LIABLE FOR ANY CLAIM, DAMAGES, OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF, OR IN CONNECTION WITH THE SKILL OR THE USE OR OTHER DEALINGS IN
THE SKILL.

LICENSE VIOLATIONS
------------------
Any violation of this license, particularly the AI/ML training prohibition,
constitutes copyright infringement and may result in:

1. Immediate termination of all licenses granted herein
2. Legal action to enforce copyright and seek damages
3. Injunctive relief to prevent ongoing violations
4. Recovery of attorneys' fees and costs

PERMISSION REQUESTS
-------------------
To request permission for uses prohibited under this license, contact:

{contact_info}

GOVERNING LAW
-------------
This license shall be governed by and construed in accordance with the laws of
{jurisdiction}, without regard to its conflict of law provisions.

Any disputes arising under this license shall be subject to the exclusive
jurisdiction of the courts located in {jurisdiction}.

================================================================================
Last Updated: {date}
License Version: 1.0
Copyright Holder{plural}: {entity_name}
"""
    return template


def create_ownership_statement(entity_type, entity_name, secondary_entity=None):
    """Create appropriate ownership statement based on entity type"""
    if secondary_entity:
        primary_type = entity_type.replace('_', ' ').title()
        return f"This work is jointly owned by {entity_name} ({primary_type}) and {secondary_entity}."
    elif entity_type == "individual":
        return ""
    elif entity_type == "corporation":
        return f"This work is owned by {entity_name}, a corporation."
    elif entity_type == "llc":
        return f"This work is owned by {entity_name}, a limited liability company."
    elif entity_type == "medical_corporation":
        return f"This work is owned by {entity_name}, a medical corporation."
    else:
        return ""


def apply_license(skill_path, entity_name, entity_type, jurisdiction,
                 contact_email=None, contact_name=None, secondary_entity=None):
    """Apply protective license to a skill"""
    skill_path = Path(skill_path).resolve()

    # Validate skill directory
    if not skill_path.exists():
        print(f"❌ Error: Skill directory not found: {skill_path}")
        return False

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        return False

    # Prepare license content
    template = load_license_template()

    # Determine pluralization
    is_joint = secondary_entity is not None
    plural = "s" if is_joint else ""
    PLURAL = "S" if is_joint else ""

    # Format entity name for joint ownership
    if secondary_entity:
        full_entity_name = f"{entity_name} and {secondary_entity}"
    else:
        full_entity_name = entity_name

    # Format contact information
    if contact_name and contact_email:
        contact_info = f"{contact_name}\n{entity_name}\nEmail: {contact_email}"
    elif contact_email:
        contact_info = f"{entity_name}\nEmail: {contact_email}"
    else:
        contact_info = f"{entity_name}\n[Contact information to be provided]"

    # Create ownership statement
    ownership = create_ownership_statement(entity_type, entity_name, secondary_entity)

    # Fill in the template
    license_content = template.format(
        year=datetime.now().year,
        entity_name=full_entity_name,
        ownership_statement=ownership,
        plural=plural,
        PLURAL=PLURAL,
        contact_info=contact_info,
        jurisdiction=jurisdiction,
        date=datetime.now().strftime("%B %d, %Y")
    )

    # Write LICENSE.txt
    license_path = skill_path / "LICENSE.txt"
    try:
        license_path.write_text(license_content)
        print(f"✅ Created LICENSE.txt in {skill_path}")
    except Exception as e:
        print(f"❌ Error writing LICENSE.txt: {e}")
        return False

    # Update SKILL.md frontmatter
    try:
        skill_content = skill_md.read_text()

        # Check if license field already exists
        if "license:" not in skill_content:
            # Add license field after description
            pattern = r'(description:.*?)(\n---)'
            replacement = r'\1\nlicense: See LICENSE.txt for complete terms\2'
            updated_content = re.sub(pattern, replacement, skill_content, flags=re.DOTALL)

            skill_md.write_text(updated_content)
            print("✅ Updated SKILL.md with license reference")
        else:
            print("ℹ️ SKILL.md already contains license reference")
    except Exception as e:
        print(f"❌ Error updating SKILL.md: {e}")
        return False

    print(f"\n✅ Successfully applied protective license to {skill_path.name}")
    print(f"   Entity: {full_entity_name}")
    print(f"   Type: {entity_type}")
    print(f"   Jurisdiction: {jurisdiction}")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Apply protective licensing to custom skills"
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
        choices=["individual", "corporation", "llc", "medical_corporation", "joint"],
        required=True,
        help="Type of entity"
    )
    parser.add_argument(
        "--jurisdiction",
        required=True,
        help="Legal jurisdiction (e.g., 'California', 'Delaware', 'New York')"
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

    success = apply_license(
        args.skill_path,
        args.entity_name,
        args.entity_type,
        args.jurisdiction,
        args.contact_email,
        args.contact_name,
        args.secondary_entity
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()