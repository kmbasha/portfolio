# KM BASHA - DUAL PORTFOLIO DEPLOYMENT PACKAGE

## 📦 PACKAGE CONTENTS

This package contains your complete dual-portfolio website with:
- **Landing Page** - Choose ICT or ELV portfolio
- **ICT Portfolio** - 17 projects (12 pure ICT + 5 integrated)
- **ELV Portfolio** - 13 projects (8 pure ELV + 5 integrated)
- **25 Project Detail Pages** - Complete project documentation
- **Support Pages** - Competencies, GRC, Sectors

---

## 📊 PORTFOLIO BREAKDOWN

### ICT PORTFOLIO (17 Projects):

**Pure ICT (12):**
1. Enterprise Data Centers Tier 3/4
2. Server Virtualization Programs
3. Data Center Relocations
4. Cloud Migration Programs
5. Mobile Attendance (15K workers)
6. Virgin Money RPA
7. RFID Asset Tracking
8. Multi-Brand Retail Integration
9. AGS PeopleSoft Integration
10. Federal National Council ITSM
11. IBM Legacy Modernization
12. HR & Workforce Management

**Integrated - ICT Primary (5):**
13. IKEA Multi-Location (Network + CCTV)
14. HCT 18 Campuses (Network + AV)
15. Mall Technology (WiFi + CCTV)
16. Qmatic CEM (Platform + Digital Signage)
17. Healthcare Infrastructure (IT + Building Systems)

---

### ELV PORTFOLIO (13 Projects):

**Pure ELV (8):**
1. INSEAD Complete ELV
2. Corporate AV (100+ rooms)
3. Premium Building Automation
4. Enterprise Telephony (Building VoIP/Intercom)
5. Enterprise WiFi (Building Infrastructure)
6. Central Bank (Security Systems)
7. Manufacturing (Building Automation)
8. American University (Campus AV)

**Integrated - ELV Primary (5):**
9. IKEA Multi-Location (CCTV + Network)
10. HCT 18 Campuses (AV + Network)
11. Mall Technology (CCTV + WiFi)
12. Qmatic CEM (Digital Signage + Platform)
13. Healthcare Infrastructure (Building Systems + IT)

---

## 📁 FILE STRUCTURE

```
portfolio/
├── index_landing.html          ← NEW Landing page (rename to index.html)
├── ict/
│   ├── index.html             ← ICT Portfolio
│   ├── projects/
│   │   └── [25 project pages]
│   ├── competencies.html
│   ├── grc.html
│   └── sectors.html
├── elv/
│   ├── index.html             ← ELV Portfolio
│   ├── projects/
│   │   └── [25 project pages]
│   ├── competencies.html
│   ├── grc.html
│   └── sectors.html
└── [original files - keep for reference]
```

---

## 🚀 DEPLOYMENT STEPS

### STEP 1: Backup Current Site
```powershell
cd "C:\Users\kmbas\OneDrive - Bluedot Technologies\Documents\GitHub\portfolio"
# Create backup
Copy-Item * -Destination ../portfolio_backup_$(Get-Date -Format 'yyyyMMdd') -Recurse
```

### STEP 2: Extract Package
1. Download DUAL_PORTFOLIO_COMPLETE.zip
2. Extract to Downloads folder
3. You'll see: index_landing.html, ict/, elv/, projects/

### STEP 3: Deploy to Repository
```powershell
cd "C:\Users\kmbas\OneDrive - Bluedot Technologies\Documents\GitHub\portfolio"

# Remove old index.html (backup made in step 1)
Remove-Item index.html

# Copy new landing page as main index
Copy-Item "$env:USERPROFILE\Downloads\DUAL_PORTFOLIO\index_landing.html" -Destination index.html

# Copy ICT portfolio
Copy-Item "$env:USERPROFILE\Downloads\DUAL_PORTFOLIO\ict" -Destination . -Recurse -Force

# Copy ELV portfolio  
Copy-Item "$env:USERPROFILE\Downloads\DUAL_PORTFOLIO\elv" -Destination . -Recurse -Force

# Verify structure
dir
```

### STEP 4: Commit and Push
```powershell
git add .
git commit -m "Launch dual portfolio - ICT (17 projects) and ELV (13 projects)"
git push origin main
```

### STEP 5: Verify Live Site
Wait 2-3 minutes, then visit:
- **Landing:** https://kmbasha.github.io/portfolio/
- **ICT:** https://kmbasha.github.io/portfolio/ict/
- **ELV:** https://kmbasha.github.io/portfolio/elv/

---

## ✅ WHAT TO TEST

### Landing Page:
- [ ] Two portfolio cards display correctly
- [ ] Stats show: ICT (17 projects, $15M+) and ELV (13 projects, $12M+)
- [ ] Clicking ICT button goes to /ict/
- [ ] Clicking ELV button goes to /elv/

### ICT Portfolio:
- [ ] Shows "17 Projects" in header or stats
- [ ] "All Projects" button shows all 17 projects
- [ ] "By Technology" filtering works
- [ ] "By Industry" filtering works
- [ ] Each project card has "View Full Project Details" button
- [ ] Project detail pages open correctly
- [ ] "← Portfolio Home" button returns to landing page

### ELV Portfolio:
- [ ] Shows "13 Projects" in header or stats  
- [ ] "All Projects" button shows all 13 projects
- [ ] "By Technology" filtering works
- [ ] "By Industry" filtering works
- [ ] Each project card has "View Full Project Details" button
- [ ] Project detail pages open correctly
- [ ] "← Portfolio Home" button returns to landing page

### Shared Projects (5):
- [ ] IKEA appears in both ICT and ELV portfolios
- [ ] HCT appears in both ICT and ELV portfolios
- [ ] Mall Technology appears in both ICT and ELV portfolios
- [ ] Qmatic CEM appears in both ICT and ELV portfolios
- [ ] Healthcare appears in both ICT and ELV portfolios

---

## 🎯 RESUME ALIGNMENT

- **ICT Portfolio** → Use with `BashaResumeProjectandProgramManagerICT2026.pdf`
- **ELV Portfolio** → Use with `Basha__Resume_Project_Program_Manager__ELV_2026.pdf`

When applying for jobs:
1. ICT roles → Share: https://kmbasha.github.io/portfolio/ict/
2. ELV roles → Share: https://kmbasha.github.io/portfolio/elv/
3. General PM roles → Share: https://kmbasha.github.io/portfolio/ (landing page)

---

## 📝 NOTES

- All 25 projects preserved - nothing removed
- 5 projects appear in BOTH portfolios (integrated programs)
- Project detail pages identical in both portfolios
- Landing page is clean, professional, no confusion
- Easy to update - just edit relevant index.html file

---

## 🆘 TROUBLESHOOTING

**Issue:** Landing page doesn't show after deployment
**Fix:** Make sure you renamed `index_landing.html` to `index.html` in root

**Issue:** ICT/ELV pages show "File not found"
**Fix:** Make sure `ict/` and `elv/` folders are in root directory

**Issue:** Project pages don't open
**Fix:** Make sure `projects/` folder exists inside both `ict/` and `elv/`

**Issue:** Styles look broken
**Fix:** Clear browser cache (Ctrl+F5) and reload

---

**Package Created:** February 5, 2026
**Total Projects:** 25 (all preserved)
**ICT Portfolio:** 17 projects
**ELV Portfolio:** 13 projects
**Status:** Ready to deploy! 🚀
