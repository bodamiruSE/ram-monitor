import psutil
import warnings

ram = psutil.virtual_memory()

if ram.percent > 84:
    print("⚠️ your ram in 85% usage!" )
print(f"Total:     {ram.total / (1024**2):.2f} MB")
print(f"Available: {ram.available / (1024**2):.2f} MB")
print(f"Percent:   {ram.percent}% used")
