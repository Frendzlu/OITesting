## Testing
Hardcode the path to your solution folder at line 10
Your file structure should look like this:
```
| ply.exe
| poc.exe
| ...
| othertask.exe
| tests
  | ply
    | in
      | ply0.in
      | ply1.in
    | out
      | ply0.out
      | ply1.out
    | otherOptionalDirectories
      | in
        | ply0.in
        | ply1.in
      | out
        | ply0.out
        | ply1.out
  | poc
    | in
      | poc0.in
      | poc1.in
    | out
      | poc0.out
      | poc1.out
    | otherOptionalDirectories
      | in
        | poc0.in
        | poc1.in
      | out
        | poc0.out
        | poc1.out
```
The time measured via test may differ from real time (may be higher).