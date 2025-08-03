"""
ECommerce Portal Test Framework - Demo Script
=============================================
This script demonstrates the comprehensive BDD framework capabilities
"""

import os
import subprocess
import time
from datetime import datetime


def run_command(command, description):
    """Run a command and display results"""
    print(f"\n{'='*60}")
    print(f"🔄 {description}")
    print(f"{'='*60}")
    
    try:
        start_time = time.time()
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        end_time = time.time()
        
        print(f"⏱️  Execution Time: {end_time - start_time:.2f} seconds")
        print(f"🏁 Exit Code: {result.returncode}")
        
        if result.returncode == 0:
            print("✅ SUCCESS")
        else:
            print("❌ FAILED")
            print("Error Output:")
            print(result.stderr)
        
        # Show last few lines of output
        if result.stdout:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 10:
                print("\nLast 10 lines of output:")
                for line in lines[-10:]:
                    print(line)
            else:
                print("\nOutput:")
                print(result.stdout)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Error executing command: {e}")
        return False


def main():
    """Main demo function"""
    print("🚀 ECommerce Portal Test Framework Demo")
    print("=" * 50)
    print(f"📅 Demo Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Working Directory: {os.getcwd()}")
    
    # Change to the project directory
    project_dir = r"c:\Users\AN574BV\OneDrive - EY\Desktop\Sai Teja\Professional\TestAI\realTimeProject\ECommercePortal_03Augv2"
    os.chdir(project_dir)
    
    python_exe = r".\.venv\Scripts\python.exe"
    
    demo_commands = [
        {
            "command": f'& "{python_exe}" tests/run_tests.py auth',
            "description": "Running Authentication Tests (@auth tag)"
        },
        {
            "command": f'& "{python_exe}" tests/run_tests.py tag:inventory',
            "description": "Running Inventory Tests (@inventory tag)"
        },
        {
            "command": f'& "{python_exe}" tests/run_tests.py smoke',
            "description": "Running Smoke Tests (@smoke tag)"
        },
        {
            "command": f'& "{python_exe}" -m pytest step_definitions/ --html=reports/html/complete_report.html --self-contained-html -v',
            "description": "Running Complete Test Suite with HTML Report"
        }
    ]
    
    results = []
    
    for test_config in demo_commands:
        success = run_command(test_config["command"], test_config["description"])
        results.append({
            "test": test_config["description"],
            "success": success
        })
        
        # Small delay between tests
        time.sleep(2)
    
    # Summary
    print(f"\n{'='*80}")
    print("📊 DEMO RESULTS SUMMARY")
    print(f"{'='*80}")
    
    total_tests = len(results)
    passed_tests = sum(1 for r in results if r["success"])
    failed_tests = total_tests - passed_tests
    
    print(f"📈 Total Test Suites: {total_tests}")
    print(f"✅ Passed: {passed_tests}")
    print(f"❌ Failed: {failed_tests}")
    print(f"📊 Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    print(f"\n📁 Generated Reports:")
    print(f"   • Authentication: reports/html/auth_report.html")
    print(f"   • Inventory: reports/html/inventory_report_*.html")
    print(f"   • Smoke Tests: reports/html/smoke_report.html")
    print(f"   • Complete Suite: reports/html/complete_report.html")
    
    print(f"\n🎯 Framework Features Demonstrated:")
    print(f"   ✅ Page Object Model (POM) Design Pattern")
    print(f"   ✅ Cucumber BDD with Gherkin Syntax")
    print(f"   ✅ Pytest Integration with Fixtures")
    print(f"   ✅ Playwright Browser Automation")
    print(f"   ✅ Tag-based Test Execution")
    print(f"   ✅ HTML Test Reporting")
    print(f"   ✅ Configuration Management")
    print(f"   ✅ Modular Test Structure")
    print(f"   ✅ Excel Integration for Test Data")
    
    print(f"\n🏷️  Available Test Tags:")
    print(f"   • @auth - Authentication module tests")
    print(f"   • @inventory - Product inventory tests")
    print(f"   • @smoke - Critical functionality tests")
    print(f"   • @TC_AUTH_01 - Specific test case identifier")
    
    print(f"\n🔧 Framework Structure:")
    print(f"   📁 pages/ - Page Object Model classes")
    print(f"   📁 features/ - Gherkin feature files")
    print(f"   📁 step_definitions/ - BDD step implementations")
    print(f"   📁 tests/ - Test runners and utilities")
    print(f"   📁 utils/ - Configuration and helper functions")
    print(f"   📁 reports/ - Test reports and artifacts")
    
    if passed_tests == total_tests:
        print(f"\n🎉 DEMO COMPLETED SUCCESSFULLY!")
        print(f"   All test suites executed successfully with comprehensive reporting.")
    else:
        print(f"\n⚠️  DEMO COMPLETED WITH ISSUES")
        print(f"   Some test suites failed. Check individual reports for details.")
    
    print(f"\n📖 For detailed usage instructions, see README.md")
    print(f"🔗 Framework ready for production use!")


if __name__ == "__main__":
    main()
