#!/bin/bash

echo "🔍 Running Python-based validations (raw layer)..."
cd python
python *.py
cd -

echo ""

echo "🧪 Running dbt model expectations (transform layer)..."
cd dbt
dbt test
cd -