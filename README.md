# christabel-portfolio
# AI Consultant Portfolio – Proof of Concept

This repository contains a proof-of-concept system for maintaining a simple, professional web presence as an AI consultant under strict cost, hosting, and maintainability constraints.

The site is hosted on **GitHub Pages** and is designed to be easy to update, easy to understand, and easy for others to reuse.

---

## Live Site

https://cofrimpong.github.io/christabel-portfolio-poc/

---

## Problem Context

As an AI consultant, I need a professional web presence that allows potential clients to quickly understand:

- who I am  
- what services I offer  
- how to contact me  

The system must be inexpensive, easy to maintain, and redistributable so that others can reuse it with minimal setup.

---

## Key Design Decisions

### Hosting
- The site is hosted entirely on **GitHub Pages**
- No paid hosting or subscription-based platforms are used

### Cost Model
- $0 monthly cost
- No subscriptions
- No backend servers

### Maintainability
- Website content is **not hard-coded into HTML**
- All site content lives in a **single source of truth**

---

## Single Source of Truth

All website content is stored in one file:

# content.json

This file contains:
- site name and headline
- about text
- services offered
- projects / case studies
- contact information
- availability status

To update the website, only `content.json` needs to be edited.  
The HTML layout remains unchanged.

This ensures updates can be made **without manually editing generated HTML pages**, satisfying the maintainability requirement.

---

## How Updates Work

1. Edit `content.json`
2. Commit the change to the `main` branch
3. GitHub Pages automatically redeploys the site
4. The live website updates within moments

No HTML files need to be modified during normal updates.

---

## Redistributable & Beginner-Friendly

This project is designed so that a classmate can reuse it easily.

A new user can:
1. Fork or clone the repository
2. Enable GitHub Pages (main branch, root folder)
3. Edit `content.json`
4. Deploy a working site with no additional software required

Only a browser and a GitHub account are needed.

---

## AI Extension (Proof of Concept)

This system is intentionally structured so it can be extended with AI.

An AI system (local LLM or pay-per-token cloud API) can:
- read `content.json`
- update content based on natural language instructions
- commit changes back to the repository

The current implementation focuses on the core architecture rather than full AI automation.

---

## Files Overview

- `index.html` — Static page layout that reads from `content.json`
- `content.json` — Single source of truth for all site content
- `README.md` — Project documentation

---

## Summary

This project demonstrates a realistic, low-cost, and maintainable approach to creating and managing a professional AI consultant website using GitHub Pages, while meeting all stated constraints and acceptance criteria.
