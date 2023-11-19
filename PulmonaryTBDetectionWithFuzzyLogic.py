import tkinter as tk
from tkinter import ttk

# Fuzzy logic functions
def fuzzy_logic(batuk_kronis, suhu_tubuh_tinggi, keringat_tidak_normal, nafas_sesak, berat_badan_kurang, nafsu_makan_kurang, dada_sakit_ya):
    # Rule-based fuzzy inference
    rule1 = min(batuk_kronis, suhu_tubuh_tinggi, keringat_tidak_normal, nafas_sesak, berat_badan_kurang, nafsu_makan_kurang, dada_sakit_ya)  # hasil positif
    rule2 = min(batuk_kronis, suhu_tubuh_tinggi, not keringat_tidak_normal, nafas_sesak, berat_badan_kurang, nafsu_makan_kurang, dada_sakit_ya)  # hasil positif
    rule3 = min(not batuk_kronis, not suhu_tubuh_tinggi, not keringat_tidak_normal, not nafas_sesak, not berat_badan_kurang, not nafsu_makan_kurang, not dada_sakit_ya)  # hasil negatif
    rule4 = min(batuk_kronis, suhu_tubuh_tinggi, not keringat_tidak_normal, not nafas_sesak, not berat_badan_kurang, not nafsu_makan_kurang, not dada_sakit_ya)  # hasil negatif

    # Aggregation (using max)
    aggregated_result = max(rule1, rule2, rule3, rule4)

    # Defuzzification (Tsukamoto method)
    total_weighted_sum = (
        rule1 * 90 +  # Batuk
        rule2 * 70 +  # Suhu Tubuh
        rule3 * 50 +  # Nafas
        rule4 * 30    # Nafsu Makan
    )

    total_weight = (
        rule1 +
        rule2 +
        rule3 +
        rule4
    )

    # Classify the result based on the weighted average
    hasil_tb_paru = total_weighted_sum / total_weight if total_weight != 0 else 0

    if hasil_tb_paru > 50:  # Adjusted threshold to classify as "Positif TB Paru"
        return "Positif TB Paru"
    else:
        return "Negatif TB Paru"

def trapesium(x, a, b, c, d):
    if x <= a or x > d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    elif c < x <= d:
        return (-(x - d)) / (d - c)

# Rest of the code remains the same...



# GUI
class FuzzyLogicGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Inferensi Fuzzy TB Paru")
        self.create_input_widgets()
        self.create_output_widgets()

    def create_input_widgets(self):
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Input").grid(column=0, row=0, columnspan=2, pady=10, sticky="w")

        ttk.Label(input_frame, text="Nama:").grid(column=0, row=1, sticky="w", pady=5)
        self.nama_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.nama_var).grid(column=1, row=1, pady=5)

        ttk.Label(input_frame, text="Batuk:").grid(column=0, row=2, sticky="w", pady=5)
        self.batuk_var = tk.StringVar()
        ttk.Combobox(input_frame, textvariable=self.batuk_var, values=['normal', 'kronis']).grid(column=1, row=2, pady=5)

        ttk.Label(input_frame, text="Suhu Tubuh:").grid(column=0, row=3, sticky="w", pady=5)
        self.suhu_tubuh_var = tk.StringVar()
        ttk.Combobox(input_frame, textvariable=self.suhu_tubuh_var, values=['normal', 'tinggi']).grid(column=1, row=3, pady=5)

        ttk.Label(input_frame, text="Keringat:").grid(column=0, row=4, sticky="w", pady=5)
        self.keringat_var = tk.StringVar()
        ttk.Combobox(input_frame, textvariable=self.keringat_var, values=['normal', 'tidak_normal']).grid(column=1, row=4, pady=5)

        ttk.Label(input_frame, text="Nafas:").grid(column=0, row=5, sticky="w", pady=5)
        self.nafas_var = tk.StringVar()
        ttk.Combobox(input_frame, textvariable=self.nafas_var, values=['normal', 'sesak']).grid(column=1, row=5, pady=5)

        ttk.Label(input_frame, text="Berat Badan:").grid(column=0, row=6, sticky="w", pady=5)
        self.berat_badan_var = tk.StringVar()
        ttk.Combobox(input_frame, textvariable=self.berat_badan_var, values=['normal', 'kurang']).grid(column=1, row=6, pady=5)

        ttk.Label(input_frame, text="Nafsu Makan:").grid(column=0, row=7, sticky="w", pady=5)
        self.nafsu_makan_var = tk.StringVar()
        ttk.Combobox(input_frame, textvariable=self.nafsu_makan_var, values=['normal', 'kurang']).grid(column=1, row=7, pady=5)

        ttk.Label(input_frame, text="Dada Sakit:").grid(column=0, row=8, sticky="w", pady=5)
        self.dada_sakit_var = tk.StringVar()
        ttk.Combobox(input_frame, textvariable=self.dada_sakit_var, values=['tidak', 'ya']).grid(column=1, row=8, pady=5)

        ttk.Button(input_frame, text="Evaluate", command=self.evaluate_fuzzy_logic).grid(column=0, row=9, columnspan=2, pady=10)

    def create_output_widgets(self):
        output_frame = ttk.Frame(self.root, padding="10")
        output_frame.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(output_frame, text="Output").grid(column=0, row=0, pady=10, sticky="w")

        ttk.Label(output_frame, text="Hasil TB Paru:").grid(column=0, row=1, pady=5, sticky="w")
        self.hasil_tb_paru_label = ttk.Label(output_frame, text="", justify="center")
        self.hasil_tb_paru_label.grid(column=1, row=1, pady=5, sticky="n")

    def show_result_window(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("Hasil Evaluasi TB Paru")

        nama_label = ttk.Label(result_window, text="Nama: " + self.nama_var.get())
        nama_label.grid(column=0, row=0, pady=5, sticky="w")

        gejala_label = ttk.Label(result_window, text="Gejala yang Dialami:\n- Batuk: {}\n- Suhu Tubuh: {}\n- Keringat: {}\n- Nafas: {}\n- Berat Badan: {}\n- Nafsu Makan: {}\n- Dada Sakit: {}".format(
            self.batuk_var.get(), self.suhu_tubuh_var.get(), self.keringat_var.get(),
            self.nafas_var.get(), self.berat_badan_var.get(), self.nafsu_makan_var.get(), self.dada_sakit_var.get()
        ))
        gejala_label.grid(column=0, row=1, pady=10, sticky="w")

        hasil_label = ttk.Label(result_window, text="Hasil: " + self.hasil_tb_paru_label["text"], justify="center")
        hasil_label.grid(column=0, row=2, pady=5, sticky="n")

    def evaluate_fuzzy_logic(self):
        # Initialize hasil_tb_paru
        hasil_tb_paru = None

        # Fuzzification
        batuk_str = self.batuk_var.get()
        suhu_tubuh_str = self.suhu_tubuh_var.get()
        keringat_str = self.keringat_var.get()
        nafas_str = self.nafas_var.get()
        berat_badan_str = self.berat_badan_var.get()
        nafsu_makan_str = self.nafsu_makan_var.get()
        dada_sakit_str = self.dada_sakit_var.get()

        # Konversi nilai ke tipe data numerik
        # Konversi nilai kategorikal ke numerik secara manual
        batuk = 1 if self.batuk_var.get().lower() == 'kronis' else 0
        suhu_tubuh = 1 if self.suhu_tubuh_var.get().lower() == 'tinggi' else 0
        keringat = 1 if self.keringat_var.get().lower() == 'tidak_normal' else 0
        nafas = 1 if self.nafas_var.get().lower() == 'sesak' else 0
        berat_badan = 1 if self.berat_badan_var.get().lower() == 'kurang' else 0
        nafsu_makan = 1 if self.nafsu_makan_var.get().lower() == 'kurang' else 0
        dada_sakit = 1 if self.dada_sakit_var.get().lower() == 'ya' else 0  # Mengonversi 'ya' menjadi 1, 'tidak' menjadi 0

        # Pemanggilan fungsi trapesium
        batuk_kronis = trapesium(batuk, 0, 0, 1, 1)
        suhu_tubuh_tinggi = trapesium(suhu_tubuh, 0, 0, 1, 1)
        keringat_tidak_normal = trapesium(keringat, 0, 0, 1, 1)
        nafas_sesak = trapesium(nafas, 0, 0, 1, 1)
        berat_badan_kurang = trapesium(berat_badan, 0, 0, 1, 1)
        nafsu_makan_kurang = trapesium(nafsu_makan, 0, 0, 1, 1)
        dada_sakit_ya = trapesium(dada_sakit, 0, 0, 1, 1)

        # Fuzzy logic evaluation
        hasil_tb_paru = fuzzy_logic(batuk_kronis, suhu_tubuh_tinggi, keringat_tidak_normal,
                                    nafas_sesak, berat_badan_kurang, nafsu_makan_kurang, dada_sakit_ya)

        # Update hasil_tb_paru
        self.hasil_tb_paru_label.config(text=hasil_tb_paru)

        # Show the result window
        self.show_result_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = FuzzyLogicGUI(root)
    root.mainloop()
