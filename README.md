# Gra w Kółko i Krzyżyk w Pythonie

Projekt powstał na zaliczenie przedmiotu Programowanie w Pythonie podczas I semestru informatyki na Uniwersytecie Dolnośląskim DSW we Wrocławiu.
Ta prosta gra w kółko i krzyżyk została stworzona w Pythonie i jest przeznaczona do uruchomienia w terminalu. Program implementuje logikę gry w kółko i krzyżyk, gdzie dwóch graczy (reprezentowanych przez "X" i "O") wykonuje ruchy na planszy 3x3, próbując umieścić swoje znaki w liniach poziomych, pionowych lub przekątnych.

## Jak działa program?

Program jest napisany w języku Python i korzysta z klas i metod do organizacji logiki gry. Główny plik programu to `tic_tac_toe.py`. Główne elementy programu to:

- `TicTacToe`: Klasa reprezentująca grę w kółko i krzyżyk. Zawiera metody do wyświetlania planszy, sprawdzania dostępnych ruchów, wykonywania ruchów graczy, sprawdzania zwycięzcy oraz prowadzenia rozgrywki.

## Uruchamianie programu

1. Upewnij się, że masz zainstalowanego Pythona na swoim komputerze.
2. Pobierz pliki z repozytorium.
3. Otwórz terminal w folderze zawierającym pliki.
4. Uruchom program, wpisując `python ttt.py`

## Zasady gry

1. Gra odbywa się na planszy 3x3.
2. Gracze wykonują ruchy na zmianę, umieszczając swoje znaki ("X" lub "O") na wolnych polach planszy.
3. Celem jest umieszczenie trzech swoich znaków w linii poziomej, pionowej lub przekątnej.
4. Pierwszy gracz, który umieści swoje znaki w wyznaczonym układzie, wygrywa grę.
5. Jeśli wszystkie pola na planszy zostaną zapełnione, a żaden gracz nie wygra, gra kończy się remisem.

## Testy jednostkowe znajdują się w pliku `testyttt.py` w głównym folderze projektu. Aby uruchomić testy, wykonaj następujące kroki:

1. Otwórz terminal.
2. Uruchom testy, wpisując polecenie `python testyttt.py`

## Autor
Ten program został stworzony przez Piotr Świercz. 
