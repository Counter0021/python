program prostochislo;
var i, j, r, quit, count, ostatok : integer;
playGame : boolean;
begin
  playGame := True;
  while(playGame = True) do
  begin
    writeln('Введите число, чтобы узнать правильное оно или нет: ');
    readln(r);
    for i := 1 to r do
    begin
      ostatok := r mod i;
    
      if (ostatok = 0) then count := count + 1;
    end;
    if (count = 2) then
      writeln('Число: ', r, ' правильное')
    else 
      writeln('Число: ', r, ' неправильное');
    
      writeln('Чтобы выйти введите 0, если нет введите, что угодно: ');
      readln(quit);
      if (quit = 0) then
        playGame := False;
  end;
end.