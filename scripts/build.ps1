# Build a TW Blue installer.
# Must be called from root of repo
echo "Installing python packages..."
pwd
pip install -r requirements.txt
echo "done."

echo "Generating documentation..."
cd doc
python document_importer.py
python generator.py
mv license.txt documentation
mv documentation ..\src
cd ..
echo "done."

echo "Building binary..."
cd src
python setup.py build
cd ..
echo "done."
