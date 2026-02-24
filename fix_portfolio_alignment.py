#!/usr/bin/env python3
"""
PORTFOLIO ALIGNMENT FIXES
Makes all corrections to align portfolio with resumes
"""
import re
import shutil

def backup_file(filepath):
    """Create backup"""
    backup = filepath + '.backup'
    shutil.copy2(filepath, backup)
    print(f"✓ Backed up: {backup}")

def fix_all_projects_header_ict(filepath):
    """Fix ICT 'All Projects' header"""
    print(f"\n{'='*60}")
    print(f"FIX 1: ICT All Projects Header - {filepath}")
    print(f"{'='*60}")
    
    backup_file(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the header
    content = content.replace(
        "html += '<h2>All Projects (25 Major Programs • 8 Flagship)</h2>';",
        "html += '<h2>All ICT Projects (17 Programs • 6 Flagship)</h2>';"
    )
    
    # Add context paragraph after header
    old_desc = "html += '<p style=\"color: #64748b; margin-bottom: 2rem;\">Complete portfolio of enterprise technology programs delivered across 7 industries. Flagship projects represent the most comprehensive, multi-year programs with detailed documentation.</p>';"
    
    new_desc = "html += '<p style=\"color: #64748b; margin-bottom: 2rem;\">Portfolio showcases 17 major ICT programs from 300+ enterprise projects delivered over 15 years. Statistics represent career totals across all engagements. Flagship projects (🏆) are comprehensive, multi-year programs with detailed documentation.</p>';"
    
    content = content.replace(old_desc, new_desc)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Fixed 'All Projects' header to show 17 programs")
    print("✓ Added statistics context explanation")

def fix_all_projects_header_elv(filepath):
    """Fix ELV 'All Projects' header"""
    print(f"\n{'='*60}")
    print(f"FIX 2: ELV All Projects Header - {filepath}")
    print(f"{'='*60}")
    
    backup_file(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the header
    content = content.replace(
        "html += '<h2>All Projects (25 Major Programs • 8 Flagship)</h2>';",
        "html += '<h2>All ELV Projects (13 Programs • 4 Flagship)</h2>';"
    )
    
    # Add context paragraph
    old_desc = "html += '<p style=\"color: #64748b; margin-bottom: 2rem;\">Complete portfolio of enterprise technology programs delivered across 7 industries. Flagship projects represent the most comprehensive, multi-year programs with detailed documentation.</p>';"
    
    new_desc = "html += '<p style=\"color: #64748b; margin-bottom: 2rem;\">Portfolio showcases 13 major ELV programs from 250+ technology integration projects delivered over 15 years. Statistics represent career totals across all engagements. Flagship projects (🏆) are comprehensive, multi-year programs with detailed documentation.</p>';"
    
    content = content.replace(old_desc, new_desc)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Fixed 'All Projects' header to show 13 programs")
    print("✓ Added statistics context explanation")

def main():
    """Main execution"""
    import sys
    import os
    
    if len(sys.argv) < 2:
        print("Usage: python3 fix_portfolio_alignment.py <path_to_portfolio>")
        print("Example: python3 fix_portfolio_alignment.py 'C:\\Users\\kmbas\\...\\portfolio'")
        sys.exit(1)
    
    portfolio_path = sys.argv[1]
    
    if not os.path.exists(portfolio_path):
        print(f"✗ Path not found: {portfolio_path}")
        sys.exit(1)
    
    print(f"\n{'#'*60}")
    print("PORTFOLIO ALIGNMENT FIXES")
    print(f"{'#'*60}\n")
    
    # Fix ICT portfolio
    ict_index = os.path.join(portfolio_path, 'ict', 'index.html')
    if os.path.exists(ict_index):
        fix_all_projects_header_ict(ict_index)
    else:
        print(f"✗ Not found: {ict_index}")
    
    # Fix ELV portfolio
    elv_index = os.path.join(portfolio_path, 'elv', 'index.html')
    if os.path.exists(elv_index):
        fix_all_projects_header_elv(elv_index)
    else:
        print(f"✗ Not found: {elv_index}")
    
    print(f"\n{'#'*60}")
    print("FIXES COMPLETE!")
    print(f"{'#'*60}")
    print("\n✅ WHAT WAS FIXED:")
    print("  1. ICT 'All Projects' header: 25 → 17 programs")
    print("  2. ELV 'All Projects' header: 25 → 13 programs")
    print("  3. Added statistics context to both portfolios")
    print("  4. Clarified flagship project indicators")
    print("\n✅ WHAT'S ALREADY CORRECT:")
    print("  - Central Bank DR IS in portfolio (Data Center project)")
    print("  - Data Center project mentions 'Central Bank UAE'")
    print("  - Resume and portfolio stats aligned")
    print("\n📋 NEXT STEPS:")
    print("  1. Test locally: open ict/index.html in browser")
    print("  2. Verify header shows '17 Programs'")
    print("  3. Read statistics context paragraph")
    print("  4. If good, commit and push:")
    print("     git add .")
    print("     git commit -m 'Fix portfolio headers and add statistics context'")
    print("     git push origin main")
    print()

if __name__ == '__main__':
    main()
