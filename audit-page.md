# Portfolio content audit

Review of index.html, style.css, and script.js for Tarun Gautam’s personal profile page.

## Required structure

| Requirement | Status | Notes |
| --- | --- | --- |
| Page title | Met | Tarun Gautam — Portfolio |
| Main heading | Met | h1 is “Tarun Gautam” |
| About section | Met | #about |
| Skills as a list | Met | Unordered list of HTML, CSS, C, Python, Problem Solving |
| Projects with links | Met | Both projects have links. Hostel uses a PLACEHOLDER href until a real URL is added; the portfolio links to this site |
| Education, email, LinkedIn | Met | #education plus email and LinkedIn in About and Contact |
| Separate CSS and JS files | Met | No inline style attributes |
| Placeholders marked PLACEHOLDER | Met | See list below |
| No invented personal details | Met | Extra bio, GitHub, resume, phone, city, project descriptions, and missing URLs are placeholders |

## Verified details used on the page

- Name: Tarun Gautam
- College: JECRC University
- Course: B.Tech CSE
- Year: 2nd Year
- Email: tarun.25bcon1193@jecrcu.edu.in
- LinkedIn: https://www.linkedin.com/in/Tarun Gautam-003574380?utm_source=share_via&utm_content=profile&utm_medium=member_ios
- Skills: HTML, CSS, C, Python, Problem Solving
- Project 1: Hostel Digital Management System (no link provided)
- Project 2: Personal Portfolio Website (linked to this page)

## PLACEHOLDER items to replace later

Search the site for the word PLACEHOLDER. Current items:

1. Location / city in the hero card
2. Two About paragraphs (interests and extra notes)
3. GitHub profile URL
4. Resume file or URL
5. Education extras (start year, graduation year, CGPA, coursework)
6. Hostel Digital Management System description
7. Hostel Digital Management System project or repository URL
8. Personal Portfolio Website description
9. Phone number in Contact

## Styling and behavior notes

- Layout is responsive below 860px, with a mobile navigation menu.
- Light and dark themes are stored in localStorage.
- Contact form validates name, email, and message in the browser. It does not send mail.
- Project 1 links to #placeholder-hostel-project until a real URL is supplied. Project 2 links to this site.
- LinkedIn opens in a new tab. The share query string from the provided URL was kept as given.

## Suggested next edits

- Replace every PLACEHOLDER string with real copy.
- Add a GitHub URL if a public profile exists.
- Add a real project URL for Hostel Digital Management System when it is available.
- Confirm whether the LinkedIn URL should keep the utm_ tracking parameters.