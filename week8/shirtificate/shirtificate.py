from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 72, 187)
        self.set_font("helvetica", "B", 20)
        self.cell(0, 55, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    write_text(input("Write Your name: "))


def write_text(name):
    pdf = PDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", size=16)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 211, f"{name} took CS50P", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
