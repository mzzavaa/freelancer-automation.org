---
title: "Auto-Sort Your Inbox with AI"
date: 2026-05-05T10:00:00+02:00
description: "Use AI to classify incoming emails by client, urgency, and type - then route them automatically."
tags: ["automation", "email", "productivity", "ai", "inbox-management"]
draft: false
schema_type: "HowTo"
---

Your inbox is a mess. Client requests mixed with newsletters mixed with invoices mixed with spam that slipped through. You spend the first 30 minutes of every day just sorting through it all, deciding what needs attention now versus later.

AI can do this sorting for you - and it understands context, not just keywords.

## Why AI Beats Filters

Traditional email filters match keywords: "invoice" goes to the Finance folder. But what about "attached is the document we discussed" when that document is an invoice? Or "urgent" in a newsletter subject line?

AI reads the actual content and understands intent. It knows that "I need this by EOD" is urgent even without the word "urgent." It recognizes a client complaint even when phrased politely.

## Setting Up AI Email Classification

### Step 1: Define Your Categories

Keep it simple. 5-8 categories max:

- **Client Work** - Active project requests, feedback, deliverables
- **New Leads** - Inquiries from potential clients
- **Admin** - Invoices, contracts, scheduling
- **Urgent** - Anything needing same-day response
- **Reference** - Newsletters, updates, things to read later
- **Low Priority** - Can wait or might not need response

### Step 2: Write Your Classification Prompt

Here's a prompt you can use with Claude or ChatGPT:

```
Classify this email into one of these categories:
- CLIENT_WORK: Active project requests or feedback
- NEW_LEAD: Potential client inquiry
- ADMIN: Invoices, contracts, scheduling
- URGENT: Needs same-day response
- REFERENCE: Newsletters, updates to read later
- LOW_PRIORITY: Can wait or may not need response

Also extract:
- Sender name
- One-sentence summary
- Any deadline mentioned

Email:
[paste email here]
```

### Step 3: Automate the Flow

**Option A: Manual batch processing**
- Once a day, copy your unread emails into Claude
- Get classifications back
- Sort accordingly

**Option B: Zapier/Make automation**
- Trigger on new email
- Send to OpenAI/Claude API
- Apply Gmail label based on classification
- Move to appropriate folder

**Option C: Built-in AI tools**
- Gmail's AI features (if you have Google Workspace)
- Outlook's Copilot (if you have Microsoft 365)
- [SaneBox](https://sanebox.com) or [Superhuman](https://superhuman.com) for dedicated solutions

## Real Examples

**Email:** "Hey, quick question - can you send over the revised logo by tomorrow morning? Client presentation at 10am."

**AI Classification:**
- Category: CLIENT_WORK + URGENT
- Summary: Logo revision needed for client presentation
- Deadline: Tomorrow 10am

**Email:** "Thanks for your proposal. We're reviewing internally and will get back to you next week."

**AI Classification:**
- Category: NEW_LEAD
- Summary: Prospect reviewing proposal, will respond next week
- Deadline: None (follow up next week)

## The Freelancer Workflow

Here's how I'd set this up:

1. **Morning:** AI sorts overnight emails into folders
2. **First pass:** Handle URGENT items immediately
3. **Second pass:** Respond to CLIENT_WORK
4. **Batch time:** Process ADMIN items together
5. **End of day:** Skim REFERENCE folder

This turns reactive email chaos into a structured system.

## What to Watch Out For

**Confidential content** - If you're sending client emails to external AI, check your contracts. Some clients prohibit this.

**Over-automation** - Don't auto-respond based on classification. Use AI for sorting, not for writing responses to important emails.

**Edge cases** - Emails that could fit multiple categories will get classified inconsistently. Add a "Review" category for ambiguous ones.

## Start Simple

Don't build a complex system on day one. Start by:

1. Manually classifying 20 emails with AI assistance
2. See if the categories make sense for your work
3. Adjust categories based on what you actually receive
4. Then automate once the system is proven

The goal isn't inbox zero. It's knowing what needs your attention right now versus what can wait.
