# %% 

idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)

# %%

teo = ["teo", "calvo", 32, True, "casado", 2342.98]
print(teo)

#  %%
#idade
print(teo[2])

#rebda
print(teo[5])

#NOME 
print(teo[0])

# %%
idades = [28, 42, 43, 35, 39, 28, 38, 42]

print("somade idades:", sum(idades))

print("quantidade de idades:", len(idades))

print("media idades:", sum(idades)/ len(idades))

print("menor idade:", min(idades))

print("maior idade:", max(idades))

# %%

teo = ["teo calvo" , 32, 
      True, "casado",
      ["estagio", "ds jr.", "ds pl", "ds sr.", "head"],
      [1500,4000,4550,6500,10000],
      ["Ana", "maria", "Claudia"]]

print("tamanho de teo", len(teo))

teo[6][0]

# %%
tamanho = len(teo)
pos =tamanho - 1

exs = teo[pos]

teo[pos][len(exs)-1]

# %%
teo[-1][-2]

# %%

#primeiros 4 elementos
teo[:4]

# %%
teo[4][3:5]

# %%
teo[4][-2:]

#%%
#teo[ start : stop :step ]

#%%
salarios = teo[5]
salarios[::3]