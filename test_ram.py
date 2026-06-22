import psutil
import warnings

ram = psutil.virtual_memory()

if ram.percent  > 70:
	warnings.warn("your ram in 70% usage!", UserWarning)

print(f"Total:     {ram.total / (1024**2):.2f} MB")
print(f"Available: {ram.available / (1024**2):.2f} MB")
print(f"Percent:   {ram.percent}% used")
