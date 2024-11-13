import openai

# openai.api_key = "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"

def wczytaj_tresc_z_pliku(sciezka_do_pliku):
    """Funkcja wczytująca treść artykułu z pliku tekstowego."""
    with open(sciezka_do_pliku, 'r', encoding='utf-8') as plik:
        return plik.read()

def generuj_html_z_openai(tresc_artykulu, prompt):
    """Funkcja wysyłająca treść artykułu i prompt do OpenAI API, by uzyskać HTML."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "Jesteś pomocnym asystentem."},
                {"role": "user", "content": prompt + "\n\n" + tresc_artykulu}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        return response['choices'][0]['message']['content'].strip()
    
    except Exception as e:
        print(f"Wystąpił błąd podczas generowania HTML: {e}")
        return None

def zapisz_html_do_pliku(html_content, sciezka_do_pliku):
    """Funkcja zapisująca wygenerowany HTML do pliku .html."""
    with open(sciezka_do_pliku, 'w', encoding='utf-8') as plik:
        plik.write(html_content)

def main():
    # Ścieżki do plików
    sciezka_tekst = "artykul.txt"  
    sciezka_wyjscie = "artykul.html"  

    # Wczytaj treść artykułu z pliku
    tresc_artykulu = wczytaj_tresc_z_pliku(sciezka_tekst)

    # Prompt, który przekażemy do OpenAI
    prompt = (
        "Przekształć poniższy artykuł na kod HTML zgodny z poniższymi zasadami:\n"
        "• Użyj tagów HTML do strukturyzacji nagłówków, akapitów i list.\n"
        "• Wstaw znaczniki <img> w miejscach, gdzie warto umieścić obraz, z atrybutem src=\"image_placeholder.jpg\" "
        "oraz alt zawierającym opis obrazu, który może być użyty do generacji grafiki.\n"
        "• Dodaj podpisy do obrazów za pomocą odpowiedniego tagu HTML.\n"
        "• Nie dołączaj CSS ani JavaScript; kod powinien zawierać tylko to, co jest pomiędzy <body> i </body>.\n"
        "• Nie dodawaj <html>, <head>, ani <body>.\n"
        "Przekształć następującą treść artykułu na kod HTML zgodnie z powyższymi wytycznymi."
    )

    # Generujemy kod HTML na podstawie artykułu i promptu
    wygenerowany_html = generuj_html_z_openai(tresc_artykulu, prompt)

    # Sprawdzamy, czy kod HTML został wygenerowany
    if wygenerowany_html:
        # Zapisz wygenerowany HTML do pliku
        zapisz_html_do_pliku(wygenerowany_html, sciezka_wyjscie)
        print(f"HTML został wygenerowany i zapisany w {sciezka_wyjscie}.")
    else:
        print("Nie udało się wygenerować HTML.")

if __name__ == "__main__":
    main()
