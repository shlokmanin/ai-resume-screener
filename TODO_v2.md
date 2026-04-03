# Enhanced AI Resume System v2 TODO

**Approved: ATS Breakdown + Charts + Ranking**

Steps:

## 1. app.py - ATS Breakdown Logic
- [ ] Update /results/<id> POST: skills(40%), keyword(30%), project(20%), quality(10%) → ats_score, breakdown dict, rank
- [ ] Refine recs: headline, missing skills, certs, projects, content cleanup (6-7 max)
- [ ] Ensure generate_improved_resume includes ATS tips

## 2. templates/results.html - UI + Charts
- [ ] ATS score + rank badge
- [ ] Chart.js CDN pie (breakdown) + bar (skills)
- [ ] Generate button

## 3. templates/generate_resume.html - Polish
- [ ] Display ATS score
- [ ] Template dropdown functional (CSS classes)

## 4. Test & Optimize
- [ ] Full flow test
- [ ] Confirm lightweight (no new deps)

**Next: app.py ATS logic**

