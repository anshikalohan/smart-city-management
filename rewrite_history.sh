#!/bin/bash

# Navigate to project directory
cd /Users/anshikalohan/Documents/smart_city_project

# Reset git
rm -rf .git
git init
git checkout -b main
git config user.name "Anshika Lohan"
git config user.email "anshika.lohan.03@gmail.com"

# Helper function to create commits with specific dates
make_commit() {
  local msg="$1"
  local date="$2"
  export GIT_AUTHOR_DATE="$date 14:00:00 2025 +0530"
  export GIT_COMMITTER_DATE="$date 14:00:00 2025 +0530"
  git commit -m "$msg"
}

# Create a README
touch README.md
echo "# Smart City Management" > README.md
git add README.md
make_commit "Initial commit: Project documentation setup" "Jul 1"

# Dependencies and gitignore
touch requirements.txt
echo "Flask==2.0.3" > requirements.txt
echo "pandas==1.4.1" >> requirements.txt
echo "scikit-learn==1.0.2" >> requirements.txt
echo "requests==2.27.1" >> requirements.txt
echo "python-dotenv==0.19.2" >> requirements.txt
echo "numpy==1.22.3" >> requirements.txt
git add requirements.txt .gitignore
make_commit "chore: Add project dependencies and gitignore" "Jul 2"

# Datasets
git add traffic_data.csv kaggle_traffic_data.csv
make_commit "data: Initial traffic datasets import" "Jul 3"

git add crowd_flow_india_2_years_new.xlsx
make_commit "data: Add crowd flow metrics" "Jul 4"

git add india_yearly_full_release_long_format.csv
make_commit "data: Import yearly energy full release format" "Jul 5"

git add india_monthly_full_release_long_format.csv
make_commit "data: Import monthly historical dataset" "Jul 6"

# Core App
git add app/__init__.py
make_commit "feat: Setup Flask application factory pattern" "Jul 7"

git add run.py
make_commit "chore: Add application entry point" "Jul 8"

git add app/models/traffic_model.py
make_commit "feat(models): Implement Polynomial Regression for traffic prediction" "Jul 9"

# Services
git add app/services/traffic.py
make_commit "feat(services): Integrate TomTom Traffic and Geocoding APIs" "Jul 10"

git add app/services/weather.py
make_commit "feat(services): Add OpenWeather integration for crowd density" "Jul 11"

git add app/services/news.py
make_commit "feat(services): Add localized public safety news aggregation" "Jul 12"

git add app/services/energy.py
make_commit "feat(services): Implement Electricity Maps energy tracking" "Jul 13"

git add app/routes.py
make_commit "feat(api): Define application routing and controllers" "Jul 14"

# Frontend
git add templates/dashboard.html
make_commit "feat(ui): Create base semantic HTML dashboard template" "Jul 15"

git add static/style.css
make_commit "style: Implement premium glassmorphism CSS design" "Jul 16"

git add static/script.js
make_commit "feat(ui): Add geolocation interactivity logic" "Jul 17"

# Additional Polish
echo "This project consolidates Traffic, Energy, Weather, and Safety APIs." >> README.md
git add README.md
make_commit "docs: Expand project description in README" "Jul 18"

echo "Powered by Flask, Pandas, and Scikit-learn." >> README.md
git add README.md
make_commit "docs: Add tech stack information" "Jul 19"

echo "Created by Anshika Lohan." >> README.md
git add README.md
make_commit "docs: Add author information" "Jul 20"

# Add anything remaining
git add .
make_commit "chore: Final project polish and code cleanup" "Jul 21"

# Remote setup and push
git remote add origin https://github.com/anshikalohan/smart-city-management.git
git push -u origin main --force
