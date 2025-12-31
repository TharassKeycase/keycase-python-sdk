@echo off
echo Cleaning old builds...
rmdir /s /q build
rmdir /s /q dist
for /d %%d in (*.egg-info) do rmdir /s /q "%%d"

echo Installing build tool...
pip install build >nul

echo Building package...
python -m build

echo Forcing reinstall of the newly built wheel...
for %%f in (dist\*.whl) do (
    pip install "%%f" --force-reinstall
)

echo Done.
pause
