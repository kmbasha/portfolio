#!/usr/bin/env python3
"""
TESTED SCRIPT: Add Central Bank DR Project
Minimal changes to working portfolio
"""
import re
import shutil
import os

def backup_file(filepath):
    """Create backup before modifying"""
    backup = filepath + '.backup'
    shutil.copy2(filepath, backup)
    print(f"✓ Backed up: {backup}")

def add_central_bank_dr(index_file):
    """Add Central Bank DR project to index.html"""
    
    print(f"\n{'='*60}")
    print(f"Processing: {index_file}")
    print(f"{'='*60}")
    
    # Backup first
    backup_file(index_file)
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # STEP 1: Find the central-bank project
    # Look for the ManageEngine project (has "Infrastructure & IT Management" in title)
    cb_pattern = r"""(\s+{\s+id:\s*'central-bank',\s+title:\s*'Central Bank UAE - Infrastructure & IT Management'[^}]+})"""
    
    match = re.search(cb_pattern, content, re.DOTALL)
    
    if not match:
        print("✗ Could not find central-bank project!")
        return False
    
    print("✓ Found central-bank project")
    
    # STEP 2: Create the DR project entry
    dr_project = """,
            {
                id: 'central-bank-dr',
                title: 'Central Bank UAE - Tier 3 DR Infrastructure',
                description: '$4.2M mission-critical disaster recovery site with 30+ servers, VMware virtualization, EMC SAN, Cisco networking, Fortigate security. Zero downtime cutover managing 25+ specialists across 8-month deployment.',
                technologies: ['Data Center & Infrastructure', 'Network & Security'],
                industry: 'Banking & Financial Services',
                budget: '$4.2M',
                timeline: '8 months',
                team: '25+ specialists',
                highlight: true
            }"""
    
    # Insert DR project right after the central-bank project
    old_project = match.group(1)
    new_content = old_project + dr_project
    content = content.replace(old_project, new_content)
    
    print("✓ Added central-bank-dr project entry")
    
    # STEP 3: Rename central-bank to central-bank-manageengine in the ID
    content = re.sub(
        r"id:\s*'central-bank',",
        "id: 'central-bank-manageengine',",
        content,
        count=1  # Only first occurrence
    )
    
    print("✓ Renamed central-bank ID to central-bank-manageengine")
    
    # STEP 4: Update filter array - add both projects
    # Find ICT or ELV filter array
    if 'ict_project_ids' in content:
        # ICT portfolio
        old_array_pattern = r"const ict_project_ids = \[(.*?)\];"
        match = re.search(old_array_pattern, content, re.DOTALL)
        if match:
            old_ids = match.group(1)
            # Add the new IDs if not already there
            if 'central-bank-dr' not in old_ids:
                # Insert after hr-workforce (before shared projects)
                new_ids = old_ids.replace(
                    "'hr-workforce'",
                    "'hr-workforce', 'central-bank-dr', 'central-bank-manageengine'"
                )
                content = content.replace(
                    f"const ict_project_ids = [{old_ids}];",
                    f"const ict_project_ids = [{new_ids}];"
                )
                print("✓ Updated ICT filter array")
    
    elif 'elv_project_ids' in content:
        # ELV portfolio
        old_array_pattern = r"const elv_project_ids = \[(.*?)\];"
        match = re.search(old_array_pattern, content, re.DOTALL)
        if match:
            old_ids = match.group(1)
            if 'central-bank-dr' not in old_ids:
                # Insert after american-university (before shared projects)
                new_ids = old_ids.replace(
                    "'american-university'",
                    "'american-university', 'central-bank-dr', 'central-bank-manageengine'"
                )
                content = content.replace(
                    f"const elv_project_ids = [{old_ids}];",
                    f"const elv_project_ids = [{new_ids}];"
                )
                print("✓ Updated ELV filter array")
    
    # Save
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Saved: {index_file}")
    
    # Verify
    with open(index_file, 'r') as f:
        verify = f.read()
    
    dr_count = verify.count("'central-bank-dr'")
    mgmt_count = verify.count("'central-bank-manageengine'")
    
    print(f"\n{'='*60}")
    print("VERIFICATION:")
    print(f"  'central-bank-dr' appears: {dr_count} times (should be 2: data + filter)")
    print(f"  'central-bank-manageengine' appears: {mgmt_count} times (should be 2: data + filter)")
    print(f"{'='*60}\n")
    
    if dr_count >= 2 and mgmt_count >= 2:
        print("✓ UPDATE SUCCESSFUL!")
        return True
    else:
        print("✗ UPDATE MAY HAVE ISSUES - CHECK MANUALLY")
        return False

def main():
    """Main execution"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 add_central_bank.py <path_to_portfolio>")
        print("Example: python3 add_central_bank.py 'C:\\Users\\kmbas\\...\\portfolio'")
        sys.exit(1)
    
    portfolio_path = sys.argv[1]
    
    if not os.path.exists(portfolio_path):
        print(f"✗ Path not found: {portfolio_path}")
        sys.exit(1)
    
    print(f"\n{'#'*60}")
    print("CENTRAL BANK DR UPDATE SCRIPT")
    print(f"{'#'*60}\n")
    
    # Process ICT portfolio
    ict_index = os.path.join(portfolio_path, 'ict', 'index.html')
    if os.path.exists(ict_index):
        add_central_bank_dr(ict_index)
    else:
        print(f"✗ Not found: {ict_index}")
    
    # Process ELV portfolio
    elv_index = os.path.join(portfolio_path, 'elv', 'index.html')
    if os.path.exists(elv_index):
        add_central_bank_dr(elv_index)
    else:
        print(f"✗ Not found: {elv_index}")
    
    print(f"\n{'#'*60}")
    print("NEXT STEPS:")
    print(f"{'#'*60}")
    print("1. Review the changes (backups created as .backup files)")
    print("2. Test locally by opening ict/index.html in browser")
    print("3. If working, commit and push:")
    print("   git add .")
    print("   git commit -m 'Add Central Bank DR project'")
    print("   git push origin main")
    print()

if __name__ == '__main__':
    main()
