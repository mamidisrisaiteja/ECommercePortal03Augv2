# CI/CD Pipeline Documentation

## 🚀 GitHub Actions Workflows

This repository includes comprehensive CI/CD pipelines for automated testing, reporting, and deployment.

### 📋 Available Workflows

#### 1. **Main CI/CD Pipeline** (`ci-cd.yml`)
- **Triggers**: Push to main/develop, Pull Requests, Scheduled (daily), Manual dispatch
- **Features**:
  - Multi-browser testing (Chromium, Firefox, WebKit)
  - Smoke, Auth, Inventory, and Full test suites
  - HTML report generation
  - Artifact upload (screenshots, videos, reports)
  - GitHub Pages deployment
  - PR commenting with test results
  - Security scanning with Bandit

#### 2. **Documentation & Release** (`docs-release.yml`)
- **Triggers**: Release published, Manual dispatch
- **Features**:
  - MkDocs documentation generation
  - GitHub Pages deployment for docs
  - Release asset creation and upload
  - Material theme with search functionality

#### 3. **Performance Testing** (`performance.yml`)
- **Triggers**: Weekly schedule (Sundays), Manual dispatch
- **Features**:
  - Performance benchmarking
  - Load time monitoring
  - Performance report generation
  - Metrics tracking and analysis

#### 4. **Dependency Management** (`dependency-check.yml`)
- **Triggers**: Weekly schedule (Mondays), Manual dispatch
- **Features**:
  - Security vulnerability scanning
  - Dependency update checks
  - Automated issue creation for vulnerabilities
  - Safety report generation

## 🎯 Workflow Usage

### Running Tests Manually

1. **Navigate to Actions tab** in GitHub repository
2. **Select "ECommerce Portal - Test Automation CI/CD"**
3. **Click "Run workflow"**
4. **Choose test suite**: smoke, auth, inventory, or all
5. **Click "Run workflow" button**

### Test Suite Options

| Suite | Description | Markers |
|-------|-------------|---------|
| **smoke** | Critical functionality tests | `@smoke` |
| **auth** | Authentication module tests | `@auth` |
| **inventory** | Product inventory tests | `@inventory` |
| **all** | Complete test suite | All markers |

### Browser Support

Tests run across three browsers:
- **Chromium** (Chrome/Edge)
- **Firefox** 
- **WebKit** (Safari)

## 📊 Test Reports

### Automated Report Publishing

- **GitHub Pages**: Test reports published to `https://<username>.github.io/<repo>/test-reports/<run-number>/`
- **Artifacts**: Downloaded from Actions > Workflow Run > Artifacts
- **PR Comments**: Automatic test result comments on Pull Requests

### Report Types

1. **HTML Reports**: Interactive test results with pass/fail status
2. **Screenshots**: Captured on test failures
3. **Videos**: Test execution recordings
4. **Performance Reports**: Benchmark and timing data
5. **Security Reports**: Vulnerability scanning results

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `BROWSER` | Browser to use for testing | `chromium` |
| `CI` | CI environment flag | `false` |
| `GITHUB_ACTIONS` | GitHub Actions environment | `false` |

### Command Line Options

```bash
# Run tests with specific browser
pytest --browser=firefox

# Run in headless mode
pytest --headless

# Run specific test suite
pytest -m smoke

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

## 🚨 Monitoring & Alerts

### Automated Notifications

- **Failed Tests**: PR comments with failure details
- **Security Issues**: Automatic issue creation for vulnerabilities
- **Performance Degradation**: Alerts when benchmarks fail thresholds

### Dashboard Access

- **GitHub Actions**: Real-time workflow status
- **GitHub Pages**: Published test reports and documentation
- **Artifacts**: Downloadable test results and media

## 🔄 Continuous Integration Features

### Pull Request Workflow

1. **Trigger**: PR created/updated
2. **Execute**: Smoke tests across all browsers
3. **Report**: Comment with test results
4. **Gate**: Requires passing tests for merge

### Main Branch Protection

- **Required Checks**: All CI tests must pass
- **Branch Protection**: Direct pushes blocked
- **Review Required**: Code review mandatory

### Scheduled Testing

- **Daily**: Smoke tests at 6 AM UTC
- **Weekly Performance**: Sundays at 2 AM UTC
- **Weekly Security**: Mondays at 8 AM UTC

## 📈 Metrics & Analytics

### Test Metrics Tracked

- **Test Execution Time**: Per test and suite
- **Success Rate**: Pass/fail statistics
- **Browser Compatibility**: Cross-browser results
- **Performance Benchmarks**: Load times and response rates

### Reports Available

- **Test Coverage**: Functional area coverage
- **Trend Analysis**: Historical test performance
- **Failure Analysis**: Common failure patterns
- **Performance Trends**: Speed and efficiency metrics

## 🛠️ Maintenance

### Regular Tasks

- **Weekly**: Review dependency updates
- **Monthly**: Analyze test trends and optimize
- **Quarterly**: Performance baseline updates
- **As Needed**: Security patch application

### Troubleshooting

Common issues and solutions:

1. **Browser Installation**: Workflows auto-install browsers
2. **Test Flakiness**: Video/screenshot capture for debugging
3. **Performance Issues**: Headless mode in CI for speed
4. **Report Access**: Check GitHub Pages deployment status
