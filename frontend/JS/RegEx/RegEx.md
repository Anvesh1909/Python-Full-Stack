# RegEx object datatype 
- it is also known as regular expression in javascript
- regular expression can be represent as if you want to represent a string as a pattern what you are searching for then we can go with regex object datatype 
- to implement regex in javascript we can pass
    - `/regex_object/i or g`
    - i stands for case sesitive and case insensitive only one time
    - g means case-sensitive searching globally number of times 
- functions used:
    - `match()`: it is used to match and return that pattern
    - `search()`: it is used to return the indexing position of the pattern where our pattern starts. if it is not found then it will return -1

---
# Charecter classes (`[]`):
- `[ABC]` ----> either A or B or C.
- `[A-Z]` ----> All uppercase A to Z.
- `[a-z]` ----> All lowercase a to z.
- `[0-9]` ----> digits or numbers from 0 to 9.
- `[A-Za-z]` ----> All uppercase and lowercase from a to z and A to Z.
- `[A-Za-z0-9]` ----> Alpha numeric charecter.
- `[^A-Za-z0-9]` ----> only special charecter (not alpha numeric).


---
# write a javascript code for charecter classess develop 3 meaningfull usecases
---
# predefined classes in javascript
- `\s` -> only spaces
- `\S` -> Except Spaces
- `\d` -> only digits
- `\D` -> Except Digits
- `\w` -> only Alphanumeric Charecters including _
- `\W` -> except (Alphanumeric Charecters) which means special charecters
---


# Quantifiers
- `A` -> only A's
- `A+` -> min one A and more than one A's  (1 or more)
- `A*` -> min zero and more than one A's (0 or more)
- `A?` -> only one or zero A (0 or 1)
- `A{min,max}` -> reange number of A's
    - ex: `A{2,5}` min 2 A's, max 5 A's
- `A{n}` ->  n number of A's
    - ex: `A{6}` 6 A's
- `^A` -> return boolean if start string starts with A
- `A$` -> return boolean if start string ends with A
- `.` -> return all the string