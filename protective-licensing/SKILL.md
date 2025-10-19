---
name: protective-licensing
description: Comprehensive tool for applying protective intellectual property licensing to custom skills. This skill should be used when users want to protect their custom skills from AI training, establish copyright ownership (individual or corporate entities), add dual-entity licensing, ensure IP protection, or apply the Protective Skills License to prevent unauthorized use of their skill content for machine learning model training.
license: See LICENSE.txt for complete terms
---

# Protective Licensing

## Overview

This skill provides automated tools and templates for applying comprehensive intellectual property protection to custom skills, with specific emphasis on preventing unauthorized AI/ML training use while maintaining appropriate copyright control for individuals, corporations, LLCs, and joint entities.

## Quick Start

To protect a skill with comprehensive licensing:

1. **For new skills**: Run `apply_license.py` during skill creation
2. **For existing skills**: Run `update_skill_license.py` on the skill directory
3. **For custom entities**: Run `customize_license.py` with entity details

All scripts support `--help` for detailed usage information.

## Core Licensing Tasks

### Apply License to New Skill

To add protective licensing when creating a new skill:

```bash
python scripts/apply_license.py --skill-path /path/to/new-skill \
  --entity-name "Your Entity Name" \
  --entity-type individual|corporation|llc|joint \
  --jurisdiction "State/Country"
```

This will:
- Copy the protective license template to the skill as LICENSE.txt
- Update SKILL.md frontmatter to reference the license
- Customize copyright notices for the specified entity

### Update Existing Skill with License

To add protective licensing to an existing skill:

```bash
python scripts/update_skill_license.py --skill-path /path/to/existing-skill \
  --entity-name "Your Entity Name" \
  --backup true
```

This will:
- Back up existing files (if requested)
- Add LICENSE.txt with protective terms
- Update SKILL.md to include license reference
- Preserve existing skill functionality

### Customize License for Entity Type

To generate a customized license for specific entity structures:

```bash
python scripts/customize_license.py \
  --primary-entity "Company Name, Inc." \
  --secondary-entity "Holding LLC" \
  --entity-types "corporation,llc" \
  --jurisdiction "California" \
  --contact-email "legal@company.com" \
  --output-path ./customized-license.txt
```

Supports:
- Single entity (individual, corporation, LLC)
- Dual-entity joint ownership
- Multiple jurisdiction options
- Custom contact information

## Key Protection Features

### AI/ML Training Prohibition

The protective license explicitly prohibits:
- Use as training data for any AI/ML system
- Fine-tuning, pre-training, or post-training of models
- Creating embeddings or vector representations
- Retrieval-augmented generation (RAG) systems
- Data mining or scraping for AI purposes
- Synthetic data generation from skill content

### Copyright Protection

Establishes clear copyright ownership for:
- Individuals
- Corporations (C-Corp, S-Corp, Medical Corp)
- Limited Liability Companies
- Joint entity ownership structures
- International entities

### Commercial Use Controls

Requires explicit written permission for:
- Commercial use of the skill
- Redistribution through marketplaces
- Creation of derivative works
- Modification without authorization

## Entity Configuration Examples

### Individual Developer
```python
entity_config = {
    "name": "Jane Doe",
    "type": "individual",
    "jurisdiction": "New York",
    "email": "jane@example.com"
}
```

### Corporate Entity
```python
entity_config = {
    "name": "TechCorp, Inc.",
    "type": "corporation",
    "jurisdiction": "Delaware",
    "email": "legal@techcorp.com"
}
```

### Joint Ownership (Medical Corporation + LLC)
```python
entity_config = {
    "primary": {
        "name": "James H. Rosing, MD, INC",
        "type": "medical_corporation",
        "jurisdiction": "California"
    },
    "secondary": {
        "name": "Tacit Investments, LLC",
        "type": "llc",
        "jurisdiction": "Delaware"
    },
    "contact": {
        "name": "James Rosing",
        "email": "jamesrosing@gmail.com"
    }
}
```

## Validation and Compliance

Run validation to ensure proper license application:

```bash
python scripts/validate_licensing.py --skill-path /path/to/skill
```

Validates:
- LICENSE.txt exists and is properly formatted
- SKILL.md includes license reference
- Copyright notices are consistent
- AI training prohibition is included
- Entity information is complete

## Resources

### scripts/

The following automation scripts are included:

- `apply_license.py` - Apply protective license to new skills
- `update_skill_license.py` - Add license to existing skills
- `customize_license.py` - Generate entity-specific licenses
- `validate_licensing.py` - Validate proper license application

### references/

License templates and documentation:

- `PROTECTIVE-SKILLS-LICENSE-TEMPLATE.txt` - Base protective license template
- `licensing-guide.md` - Comprehensive guide to applying protective licensing
- `entity-structures.md` - Guide for different entity types and jurisdictions
- `ai-training-prohibition.md` - Detailed explanation of AI/ML training restrictions

### Keywords

protective licensing, IP protection, copyright, AI training prohibition, skill licensing, intellectual property, custom skills, entity licensing, dual-entity, joint ownership, commercial restrictions, open source protection