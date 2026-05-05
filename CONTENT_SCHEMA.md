# Content Schema Contract

This document defines the front matter fields, section purposes, and naming conventions for content submitted to the freelancer-automation-site.

## Base front matter (required on every page)

- `title` (string)
- `date` (ISO 8601 datetime)
- `description` (string, max 160 chars)
- `tags` (array of strings)
- `draft` (boolean)

## Optional common fields

- `schema_type` (enum: `Article`, `HowTo`, `SoftwareSourceCode`, `Course`, `FAQPage`)
- `faq` (array of objects `{question, answer}`)
- `generated_by` (string)
- `source_refs` (array of strings)

## Section-specific extensions

### daily/

- `pillar` (slug of a guide page, optional)

Filename pattern: `YYYY-MM-DD-slug.md`.

### guides/

Guide pages are pillars; other content may reference them via `pillar`.

### open-source/

- `pillar` (optional)
- `github_url` (URL)
- `language` (string)
- `license` (string)
- `install_command` (string)

### build-log/

No extra fields beyond base.

### workshops/

- `price` (string)
- `format` (`online`, `in-person`, `hybrid`)
- `duration` (string)
- `booking_url` (URL)

## Validation rules

- `description` max 160 characters
- `schema_type` must be one of the allowed enum values
- workshop `format` must be one of the listed options

When automated pipelines commit content they should adhere to these conventions.
