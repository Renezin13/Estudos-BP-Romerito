CREATE TABLE IF NOT EXISTS tb_jogador (
   jog_id INTEGER PRIMARY KEY AUTOINCREMENT,
   jog_nome TEXT NOT NULL,
   jog_class TEXT,
   jog_vida INTEGER
);

CREATE TABLE IF NOT EXISTS tb_monstro (
   mon_id INTEGER PRIMARY KEY AUTOINCREMENT,
   mon_nome TEXT NOT NULL,
   mon_tipo TEXT,
   mon_vida INTEGER
);
