# ShipGameServer

## Dokumentacja użytkownika

* Do uruchomienia serwer wystarczy tylko komenda ``python main.py``

## Dokumentacja techniczna

1. Głowny folder
    - main.py - Główny plik startowy, gdzie mapujemy kontrolery, a następnie uruchamiamy serwer
    - App.py - Głowny plik serweru
        - sock - zmienna przchwująca połączenie
        - endpoints - słownik z kontrolerami
        - map_controller - mapuje kontroler przekazany w argumencie
        - run - uruchamia serwer socket i nasłuchuje na połączenie, następnie kieruje ruch do odpowiedniej metody
        - close - zamyka serwer
        - call_endpoint - woła odpowiedni endpoint w kontrolerze
2. Endpoints
   - BaseController.py - Bazowa kalsa kontrolera
     - basePath - ścieżka do kontrolera
     - actions - akcje dostępne w kontrolerze
   - GameController.py - Kontroler dla gier
     - join_to_game - metoda obsługująca próbę dołączenia do gry
     - can_game_start - metoda zwracająca informację czy gra może się zacząć
     - get_game_data - metoda pobierająca dane z gry
     - ready - metoda ustawiająca godowość gracza jak który zgłasza gotowość
     - move - metoda która obsługuje ruch gracza
     - close - metoda kończoca grę
   - GameRoomsController - kontroler do obsługi pokojów gier
     - get_all - zwraca listę wszystkich dostępnych gier
     - create_room - metoda, która tworzy pokój
   - PlayerController.py - kontroler do obsługi gracza
     - join_to_server - metoda, która dodaje garcza na serwer
     - exit - metoda, która służy do rozłączenia garacza z serwerem.
3. Models - folder z modelami
   - Game - Model Gry
     - player1 - Gracz 1
     - player2 - Gracz 2
     - moving_player - gracz który obecnie ma ruch
     - game_phase - obecny status gry
     - winning_player_name - nazwa gracza który wygrał
     - name - nazwa gry
     - can_other_player_join - metoda zwraca True, jeśli drugi gracz może dołączyć do gry
     - join - metoda służąca do dołączenia do gry
     - set_game_phase - metoda, która ustawia fazę gry
     - game_can_start - metoda, która zwraca Ture jeśli gra może się rozpocząć
     - get_game_data - metoda, która zwraca dane z gry
     - move - metoda, która jest do obsługi ruchu gracza 
     - verify_result - metoda sprawdzająca czy gracz wygrał
     - close_game - metoda kończąca grę
     - remove_player - metoda usuwająca gracza z pokoju
     - can_remove - metoda sprawdzająca, czy można usunąć pokój
   - Player - Model gracza
     - name - nazwa gracza
     - player_board - plansza gracza z ustawionymi statkami
     - player_hit - plansza gracza z trafieniami
     - ready - flaga mówiąca o tym, czy gracz jest gotowy
4. Store - folder z storami
    - GameStore.py - store z grami
      - games - lista gier
      - add_game - metoda dodaje nową grę
      - get_all - metoda pobiera wszystkie gry
      - find_by_name - metoda zwraca grę po nazwie
      - remove_game - metoda usuwająca grę z stora
      - exists_by_name - metoda sprawdzająca, czy gra o danej nazwie istnieje
      - remove_all_player_game - metoda usuwająca wszystkie gry gracza
    - PlayerStore.py - store z graczami
      - players - lista graczy
      - find_by_name - szuka gracza po nazwie
      - remove_player - usuwa gracza
