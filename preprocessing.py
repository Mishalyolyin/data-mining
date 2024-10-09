import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
file_path = r'datakelulusanmahasiswa.xlsx'  # Adjust the path if needed
data = pd.read_excel(file_path)

# Mengisi nilai yang hilang menggunakan SimpleImputer
# Untuk kolom numerik, menggunakan nilai rata-rata (mean) misalnya 'IPS 1' dan 'IPS 2'
imputer = SimpleImputer(missing_values=pd.NA, strategy='mean')
data[['IPS 1', 'IPS 2']] = imputer.fit_transform(data[['IPS 1', 'IPS 2']])

# Untuk kolom kategorikal, menggunakan nilai yang paling sering (modus)
imputer_categorical = SimpleImputer(strategy='most_frequent')
data['STATUS KELULUSAN'] = imputer_categorical.fit_transform(data[['STATUS KELULUSAN']]).ravel()
data['JENIS KELAMIN'] = imputer_categorical.fit_transform(data[['JENIS KELAMIN']]).ravel()

# Membulatkan kolom 'IPS 1' dan 'IPS 2' menjadi dua digit
data['IPS 1'] = data['IPS 1'].round(2)
data['IPS 2'] = data['IPS 2'].round(2)

# Cek jika ada nilai yang masih 0 di IPS 1 dan IPS 2
print("IPS 1 sebelum disimpan:", data['IPS 1'].unique())
print("IPS 2 sebelum disimpan:", data['IPS 2'].unique())

# Define output paths
output_excel_path = r'C:\Users\User\OneDrive\Desktop\mata kuiah\semester 5\data mining\tugas\datakelulusanmahasiswa_cleaned.xlsx'
output_csv_path = r'C:\Users\User\OneDrive\Desktop\mata kuiah\semester 5\data mining\tugas\datakelulusanmahasiswa_cleaned.csv'

# Save the cleaned data to Excel and CSV
data.to_excel(output_excel_path, index=False)
data.to_csv(output_csv_path, index=False)

print(f"Data preprocessing selesai. Hasil disimpan ke {output_excel_path} dan {output_csv_path}.")
