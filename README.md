# Python_application_html

# Aplikacja do Generowania HTML z Artykułu

## Opis zadania
Aplikacja napisana w Pythonie, która wykorzystuje OpenAI API do przekształcenia artykułu tekstowego na kod HTML. Aplikacja przekształca zwykły tekst artykułu na stronę HTML, strukturalizując treść za pomocą odpowiednich tagów HTML (takich jak nagłówki, akapity, obrazy i podpisy pod obrazkami). Program umożliwia wygodne generowanie zawartości HTML w pełni zautomatyzowanym procesie.

## Cel
Celem aplikacji jest:
1. Połączenie z API OpenAI.
2. Odczytanie pliku tekstowego zawierającego artykuł.
3. Przesłanie artykułu do API OpenAI w celu uzyskania odpowiedzi, która będzie zawierała kod HTML.
4. Zapisanie wygenerowanego kodu HTML w pliku `.html`.

## Zasady Generowania HTML
Wygenerowany kod HTML zawiera:
- Strukturalne tagi HTML takie jak nagłówki (`<h1>`, `<h2>`, itd.), akapity (`<p>`).
- Miejsca na obrazy oznaczone tagiem `<img src="image_placeholder.jpg" alt="Opis obrazu">`.
- Opis obrazu (tekst do użycia w generacji grafik) w atrybucie `alt` każdego obrazu.
- Podpisy pod obrazkami w odpowiednich tagach HTML.

Nie zawiera żadnego kodu CSS ani JavaScript, ponieważ program generuje jedynie część HTML pomiędzy tagami `<body>` i `</body>`.

## Instrukcje Uruchomienia

### Krok 1: Instalacja Zależności
Przed uruchomieniem aplikacji musisz zainstalować bibliotekę `openai`. W tym celu uruchom poniższą komendę:

```
pip3 install openai==0.28 
```
* jeśli posiadasz zainstalowany python3.
* natomiast, jeśli posiadasz zainstalowany python2, komenda będzie wyglądała w ten sposób:

```
pip install openai==0.28
```

## Krok 2: Uzyskanie klucza API 
Aby aplikacja mogła korzystać z OpenAI API, musisz posiadać ważny klucz API. 
Uzyskaj go rejestrując się na platformie OpenAI. 
Po otrzymaniu klucza, wstaw go do kodu w pliku ```main.py```:
```
openai.api_key = "Twój_Klucz_API"
```

## Krok 3: Przygotowanie Pliku Artykułu
W aplikacji artykuł jest wczytywany z pliku tekstowego ```artykul.txt```. 
Wczytany plik tekstowy zostanie przesłany do OpenAI API, które zwróci kod HTML.

## Krok 4: Uruchomienie Aplikacji
Po przygotowaniu artykułu i ustawieniu klucza API, uruchom aplikację za pomocą poniższej komendy:
```
python3 main.py
```
* jeśli posiadasz zainstalowany python3.
* natomiast, jeśli posiadasz zainstalowany python2, komenda będzie wyglądała w ten sposób:
```
python main.py
```


## Krok 5: Wygenerowany Plik HTML
Po pomyślnym wykonaniu skryptu, wygenerowany plik HTML będzie zapisany w katalogu głównym projektu jako ```artykul.html```. 
W pliku tym będzie znajdować się treść artykułu przekształcona na kod HTML z odpowiednimi tagami i obrazami.

### Struktura Repozytorium
Repozytorium zawiera następujące pliki:
* ``` main.py ``` – Główny plik aplikacji, który zawiera kod do przetwarzania artykułu i generowania HTML.
* ``` artykul.txt ``` – Przykładowy artykuł w formacie tekstowym, który zostanie użyty w aplikacji.
* ``` artykul.html ``` – Wygenerowany plik HTML, zawierający kod HTML na podstawie artykułu.
* ``` szablon.html ``` – szablon HTML dla wizualizacji artykułów (sekcja zadania dodatkowego).
* ``` podglad.html ``` – plik z pełnym podglądem artykułu (sekcja zadania dodatkowego).
* ``` README.md ``` – Plik dokumentacji, który zawiera informacje o projekcie oraz instrukcje uruchomienia aplikacji.

## Zasady i Wytyczne
* Aplikacja generuje HTML zgodny z wytycznymi określonymi w zadaniu.
* Użycie tagów HTML takich jak `<h1>`, `<h2>`, `<ul>`, `<p>`, `<img>`, z odpowiednimi atrybutami, w tym alt do obrazów.
* Aplikacja nie generuje kodu CSS ani JavaScript, lecz tylko czysty HTML w sekcji `<body>`.
* Każdy obraz w artykule jest reprezentowany przez tag `<img>` z tekstem opisującym obraz w atrybucie `alt`.


# Zadanie dla chętnych: Szablon HTML do podglądu artykułu

## Opis zadania
Dla wzbogacenia projektu, opracowany został prosty szablon HTML w pliku ```szablon.html```, który umożliwia wizualizację artykułu po wklejeniu jego kodu HTML w sekcji ```<body>```. Dodatkowo, pełny podgląd artykułu wygenerowany po wklejeniu treści ```artykul.html``` do ```szablon.html``` zapisano jako ```podglad.html```.

## Struktura plików
* ``` szablon.html ``` – szablon HTML gotowy do wstawienia treści artykułu.
* ``` podglad.html ``` – końcowy podgląd z wklejoną treścią ``` artykul.html ```.

## Instrukcja
1. Skopiuj wygenerowaną zawartość pliku ``` artykul.html ``` do sekcji ``` <body> ``` w pliku ```szablon.html```.
2. Zapisz skopiowany plik jako ``` podglad.html ```, aby uzyskać pełen podgląd artykułu.

## Przykład użycia
1. W pliku ```szablon.html``` zdefiniowane zostały style CSS oraz prosty kod w JavaScript umożliwiający łatwe wklejenie wygenerowanego kodu HTML artykułu i podgląd.
2. Wklej zawartość ``` artykul.html ``` do ``` <body> ``` pliku ``` szablon.html ``` i zapisz jako ``` podglad.html ```, aby móc otworzyć go i zobaczyć pełny podgląd artykułu.

## Uwagi
Szablon ``` szablon.html ``` nie zawiera żadnych treści początkowych w ``` <body> ```, więc można bezpośrednio wklejać tam wygenerowany kod ``` artykul.html ``` bez ryzyka nadpisania innej treści.

### Autor Projektu: Klaudia Czechowska 









