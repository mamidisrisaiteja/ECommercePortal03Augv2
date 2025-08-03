"""Test runner for executing BDD tests"""
import pytest
import sys
import os
from datetime import datetime


def run_auth_tests():
    """Run authentication tests"""
    args = [
        "step_definitions/test_authentication_steps.py",
        "-m", "auth",
        "--html=reports/html/auth_report.html",
        "--self-contained-html",
        "-v"
    ]
    return pytest.main(args)


def run_smoke_tests():
    """Run smoke tests"""
    args = [
        "step_definitions/",
        "-m", "smoke", 
        "--html=reports/html/smoke_report.html",
        "--self-contained-html",
        "-v"
    ]
    return pytest.main(args)


def run_all_tests():
    """Run all tests"""
    args = [
        "step_definitions/",
        "--html=reports/html/full_report.html",
        "--self-contained-html",
        "-v"
    ]
    return pytest.main(args)


def run_tests_by_tag(tag):
    """Run tests by specific tag"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"{tag}_report_{timestamp}.html"
    
    args = [
        "step_definitions/",
        "-m", tag,
        f"--html=reports/html/{report_name}",
        "--self-contained-html",
        "-v"
    ]
    return pytest.main(args)


if __name__ == "__main__":
    print("🚀 ECommerce Portal Test Runner")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        test_type = sys.argv[1].lower()
        
        if test_type == "auth":
            print("Running Authentication Tests...")
            exit_code = run_auth_tests()
        elif test_type == "smoke":
            print("Running Smoke Tests...")
            exit_code = run_smoke_tests()
        elif test_type == "all":
            print("Running All Tests...")
            exit_code = run_all_tests()
        elif test_type.startswith("tag:"):
            tag = test_type.split(":")[1]
            print(f"Running tests with tag: {tag}")
            exit_code = run_tests_by_tag(tag)
        else:
            print(f"Unknown test type: {test_type}")
            print("Available options: auth, smoke, all, tag:<tag_name>")
            exit_code = 1
    else:
        print("Running Authentication Tests (default)...")
        exit_code = run_auth_tests()
    
    print(f"\n✅ Tests completed with exit code: {exit_code}")
    print(f"📊 Check reports in: reports/html/")
    
    sys.exit(exit_code)
