# halloween-ljud

Skräckljud för Halloween-skrämman i Home Assistant, servade via jsDelivr så att Google Cast-högtalarna kan hämta dem snabbt:

```
https://cdn.jsdelivr.net/gh/vkardell/halloween-ljud@v5/<fil>.mp3
```

## Filerna

Elva MP3:or (192 kbit/s, 44,1 kHz) från archive.org-paketet
[Ringtonehorrorscreamssoundeffect270204](https://archive.org/details/Ringtonehorrorscreamssoundeffect270204).
Paketet anger ingen licens.

Originalen börjar med 2,75–4,0 s tystnad. Här är tystnaden bortklippt så att ljudet börjar efter cirka 0,1 s.
Klippningen sker på MP3-ramgränser utan omkodning, så resten av ljudet är bit för bit identiskt med originalet.

`diabolical_laugh_3x.mp3` är det elaka skrattet tre gånger i rad, gjort med
`make_loop_mp3.py diabolical_laugh.mp3 diabolical_laugh_3x.mp3 3 --end 5.6`.
Originalet slutar med 2,7 s tystnad. Den är bortklippt så att det bara blir cirka 0,4 s mellan skratten.

## Musiken

I `musik/` ligger spåren som loopas efter skrämman tills grinden laddar om.

Fyra spår är oförändrade från incompetech.com:

- "Myst on the Moor" Kevin MacLeod (incompetech.com)
- "Gathering Darkness" Kevin MacLeod (incompetech.com)
- "Ghost Story" Kevin MacLeod (incompetech.com)
- "Spellbound" Kevin MacLeod (incompetech.com)

Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/

Fem speldosespår kommer från OpenGameArt. De är omkodade till MP3 med `make_loop_mp3.py`, och de som loopar sömlöst är upprepade några gånger i filen så att det blir färre pauser när Home Assistant startar om spåret:

- `forgotten_lullaby.mp3`: "Forgotten Lullaby" (Music Box Loop, 8 gånger). Music by Mega Pixel Music Lab, megapixelmusiclab.com. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Källa: https://opengameart.org/content/forgotten-lullaby
- `broken_carousel_waltz.mp3`: Music: "Broken Carousel Waltz" by Arold Valda. Licensed under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Källa: https://opengameart.org/content/broken-carousel-waltz
- `sad_tune.mp3` (2 gånger) och `spooky_waltz.mp3` (2 gånger): "musicbox3_sad_tune" och "musicbox1_spooky_waltz" av Aureolus_Omicron. CC0. Källa: https://opengameart.org/content/4-music-box-tracks
- `creepy_lullaby.mp3`: "Creepy lullaby (short)" av iletzy (11 gånger). CC BY-SA 3.0, https://creativecommons.org/licenses/by-sa/3.0/. Den upprepade filen delas under samma licens. Källa: https://opengameart.org/content/creepy-lullaby-short

Sju ljudmattor (vind, djur, spöken) kommer från Freesound, alla CC0. Freesound släpper bara originalen till inloggade, så källan är deras offentliga förhandsfil (MP3, 128 kbit/s).
De loopar inte av sig själva, så in- och uttoningen är bortklippt och varje varv tonar över i nästa under 3 s, till cirka 5–7 min per fil.
Två var mycket svagare än resten och är höjda:

| Fil | Original | Klippt (s) | Varv | Höjd |
|---|---|---|---|---|
| `dark_horror_forest.mp3` | "Dark Horror Forest Soundscape" av szegvari, https://freesound.org/s/580453/ | 2,5–71 | 5 | |
| `witch_forest.mp3` | "Witch forest Atmo" av szegvari, https://freesound.org/s/577936/ | 2,5–137,5 | 3 | |
| `spooky_owls.mp3` | "Perfect Spooky Owls" av DreamSavvyr, https://freesound.org/s/787733/ | 2–68,5 | 5 | +5 dB |
| `graveyard.mp3` | "Graveyard" av NeoSpica, https://freesound.org/s/504620/ | 9–101 | 4 | +11 dB |
| `spooky_wind.mp3` | "Spooky Wind" av PearceWilsonKing, https://freesound.org/s/256607/ | 0–111 | 3 | |
| `dark_house.mp3` | "Little dark house soundscape" av szegvari, https://freesound.org/s/557191/ | 2–140 | 3 | |
| `ghosts_at_home.mp3` | "Ghosts at Home?" av ChristmasKrumble666, https://freesound.org/s/852791/ | 0,5–75,5 | 5 | |

## Göra en loopfil

```
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python make_loop_mp3.py original.ogg musik/namn.mp3 <antal varv> [--crossfade s] [--start s] [--end s] [--gain-db dB]
```

Ljudmattorna ovan är gjorda med `--crossfade 3` och klippningen och höjningen i tabellen,
t.ex. `make_loop_mp3.py graveyard.mp3 musik/graveyard.mp3 4 --crossfade 3 --start 9 --end 101 --gain-db 11`.

## Klippa en ny fil

```
python3 trim_mp3.py original.mp3 klippt.mp3 <sekunder att ta bort>
```

Skriptet hanterar bara CBR-MP3 i 44,1 kHz (som filerna i paketet) och har inga beroenden utöver Python 3.
Sätt sekunderna till tiden för första hörbara ljud minus 0,1.

Efter en ändring: committa, skapa en ny tagg (`v6` osv.) och peka om URL:erna i Home Assistant till den taggen.
jsDelivr cachar en tagg för alltid.
