import pandas as pd


def convert_column_to_float64(column_data_frame: pd.DataFrame,
                              default: float) -> pd.DataFrame:
    return column_data_frame.apply(
        lambda num:
        num
        if str(num).isnumeric()
        else str(num).replace(",", ".")
        if str(num).replace(",", ".").isnumeric()
        else default
    ).astype("float64")


def convert_column_to_int64(column_data_frame: pd.DataFrame,
                            default: int) -> pd.DataFrame:
    return column_data_frame.apply(
        lambda num:
        num
        if str(num).isnumeric()
        else default
    ).astype("int64")


if __name__ == '__main__':

    print(f"\n\nExercícios parte 1\n")

    filename = "./Datasets/Imóveis.csv"

    # exercício 1
    frame = pd.read_csv(filename, sep=",")

    # exercício 2
    print(f"\n# exercício 2:\n{frame.shape}")

    # exercício 3
    print(f"\n# exercício 3:\n{frame.head(10)}")

    # exercício 4
    print(f"\n# Exercício 4:\n{frame.columns}")

    # exercício 5
    print(f"\n# exercício 5:\n{frame.dtypes}")

    # exercício 6
    frame["data"] = pd.to_datetime(frame["data"])

    # exercício 7
    frame["análise"] = 2021

    # exercício 8
    print(f"\n# exercício 8:\n{pd.DataFrame(frame, columns=['id', 'data', 'preço', 'quartos', 'banheiros', 'ano de construção'])}")

    # exercício 9
    frame.drop(["metragem da casa.1"], axis=1)  # axis começa em 0, main axis = linha

    # exercício 10
    frame["banheiros"] = frame["banheiros"].apply(
        lambda num:
        str(num).split(",")[0]
    ).astype('int64')

    # exercício 11
    print(f"\n# exercício 11:\n{frame.loc[frame['ano de construção'] < 2000]}")

    # exercício 12
    frame = frame.rename(columns={
        "data": "DT_REFERENCIA",
        "preço": "VL_PRECO",
        "quartos": "QTD_QUARTOS",
        "banheiros": "QTD_BANHEIROS",
        "ano de construção": "DT_ANO_CONSTRUCAO",
        "código postal": "NU_CEP",
        "latitude": "NU_LATITUDE",
        "longitude": "NU_LONGITUDE",
        "andares": "QTD_ANDARES",
        "orla": "FL_ORLA",
        "vista": "FL_VISTA"
    })

    print(f"\n{frame.dtypes}")

    # exercício 13
    frame["DS_TIPO_CONDICAO"] = [
        "Ruim"
        if num < 2
        else "Regular"
        if num <= 4
        else "Bom"
        for num
        in frame["condição"]
    ]

    print(f"\n{frame['DS_TIPO_CONDICAO']}")

    frame["VL_PRECO"] = frame["VL_PRECO"].apply(
        lambda num:
        str(num).replace(",", ".")
    ).astype('float64')

    # exercício 14
    print(f"\n# exercício 14:\n{frame[['id', 'VL_PRECO']].sort_values(['VL_PRECO'])}")

    # exercício 15
    frame_filtro_1 = frame.query("DS_TIPO_CONDICAO == 'Regular'")

    print(f"\n# exercício 15:\n{frame_filtro_1.shape[0]}")

    # exercício 16
    print(f"\n# exercício 16:\n{frame_filtro_1['VL_PRECO'].mean()}")

    # exercício 17
    frame_filtro_2 = frame.query("QTD_QUARTOS == 3")

    preco_max = frame_filtro_2['VL_PRECO'].max()

    print(f"\n# exercício 17:\n{preco_max}")

    # exercício 18
    frame_filtro_3 = frame.query(
        "DS_TIPO_CONDICAO == 'Bom' and QTD_QUARTOS > 2 and QTD_BANHEIROS > 2"
    )

    print(f"\n# exercício 18:\n{frame_filtro_3}")

    # exercício 19
    preco_max = frame['VL_PRECO'].max()

    frame_casa_maior_preco = frame[frame['VL_PRECO'] == preco_max]

    print(f"\n# exercício 19:\n{frame_casa_maior_preco['id']}")

    # exercício 18
    preco_min = frame['VL_PRECO'].min()

    frame_casa_menor_preco = frame[frame['VL_PRECO'] == preco_min]

    print(f"\n# exercício 18\n{frame_casa_menor_preco['id']}")

    # exercício 19:
    print(f"\n# exercício 19:\n{frame['DT_REFERENCIA'].min()}")

    # exercícios parte 2

    print(f"\n\nExercícios parte 2\n")

    print(f"\n{frame.groupby(['DS_TIPO_CONDICAO']).size().reset_index(name='QTD_IMOVEIS')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['VL_PRECO'].mean().reset_index(name='VL_MEDIA')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['QTD_QUARTOS'].min().reset_index(name='NU_MENOR_QUARTOS')}")

    print(f"\n{frame.groupby(['QTD_QUARTOS', 'QTD_BANHEIROS'])['VL_PRECO'].sum().reset_index(name='VL_SOMATORIO')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['VL_PRECO'].median().reset_index(name='VL_MEDIANA')}")

    frame["NU_CLASSIFICACAO_PRECO_1"] = [
        0
        if num < 321950
        else 1
        if num <= 450000
        else 2
        if num <= 645000
        else 3
        for num
        in frame["VL_PRECO"]
    ]

    print(f"\n{frame.head()}")

    frame["NU_CLASSIFICACAO_PRECO_2"] = frame["VL_PRECO"].apply(
        lambda num:
        0
        if num < 321950
        else 1
        if num <= 450000
        else 2
        if num <= 645000
        else 3
    )

    print(f"\n{frame.head()}")

    media_preco = pd.DataFrame({
        "id": [x for x, y in enumerate(frame.groupby(["NU_CEP"]))],
        "VL_MEDIA_PRECO": frame.groupby(["NU_CEP"])["VL_PRECO"].mean()
    }).reset_index()

    print(f"{media_preco}")

    media_preco.to_csv("./Datasets/Imóveis2.csv", index=False)

    # exercícios parte 3

    print(f"\n\nExercícios parte 3\n")

    # exercício 1
    path_cadastro_loja_a = "./Datasets/CadastroLoja_A.xlsx"
    path_cadastro_loja_b = "./Datasets/CadastroLoja_B.xlsx"
    path_tipo_cliente = "./Datasets/TipoCliente.xlsx"
    path_vendas = "./Datasets/Vendas.xlsx"

    data_frame_cadastro_loja_a = pd.DataFrame(
        pd.read_excel(
            path_cadastro_loja_a
        )
    )

    data_frame_cadastro_loja_b = pd.DataFrame(
        pd.read_excel(
            path_cadastro_loja_b
        )
    )

    data_frame_tipo_cliente = pd.DataFrame(
        pd.read_excel(
            path_tipo_cliente
        )
    )

    data_frame_vendas = pd.DataFrame(
        pd.read_excel(
            path_vendas
        )
    )

    # print(f"\n{data_frame_cadastro_loja_a}")
    # print(f"\n{data_frame_cadastro_loja_b}")
    # print(f"\n{data_frame_tipo_cliente}")
    # print(f"\n{data_frame_vendas}")

    # exercício 2
    print(f"\n# exercício 2:\nLOJA A:\n{data_frame_cadastro_loja_a.head()}")
    print(f"\n{data_frame_cadastro_loja_a.shape}")
    print(f"\n{data_frame_cadastro_loja_a.dtypes}")

    print(f"\nLOJA B:\n{data_frame_cadastro_loja_b.head()}")
    print(f"\n{data_frame_cadastro_loja_b.shape}")
    print(f"\n{data_frame_cadastro_loja_b.dtypes}")

    print(f"\nTIPO CLIENTE:\n{data_frame_tipo_cliente.head()}")
    print(f"\n{data_frame_tipo_cliente.shape}")
    print(f"\n{data_frame_tipo_cliente.dtypes}")

    print(f"\nVENDAS:\n{data_frame_vendas.head()}")
    print(f"\n{data_frame_vendas.shape}")
    print(f"\n{data_frame_vendas.dtypes}")

    # exercício 3
    cliente_loja_a_vendas = data_frame_cadastro_loja_a.merge(
        data_frame_vendas,
        how="inner",
        on="ID"
    )

    print(f"\n# exercício 3\n{cliente_loja_a_vendas}")

    # exercício 4
    cliente_loja_b_vendas = data_frame_cadastro_loja_b.merge(
        data_frame_vendas,
        how="inner",
        on="ID"
    )

    print(f"\n# exercício 4:\n{cliente_loja_b_vendas}")

    # exercício 5 e 6
    cliente_cadastrado_a_b = data_frame_cadastro_loja_a.merge(
        data_frame_cadastro_loja_b,
        how="inner",
        on="ID"
    ).rename(columns={
        "Nome_x": "NO_A",
        "Nome_y": "NO_B",
        "Idade_x": "NU_IDADE_A",
        "Idade_y": "NU_IDADE_B",
        "CEP_x": "NU_CEP_A",
        "CEP_y": "NU_CEP_B",
        "TipoCliente_x": "CD_TIPO_CLIENTE_A",
        "TipoCliente_y": "CD_TIPO_CLIENTE_B"
    })

    print(f"\n# exercício 5 e 6:\n{cliente_cadastrado_a_b}")

    # exercício 7 e 8
    todos_clientes_lojas = data_frame_cadastro_loja_a.merge(
        data_frame_cadastro_loja_b,
        how="outer",
        on="ID",
        suffixes=("_A", "_B")
    ).drop_duplicates(
        subset="ID"
    )

    print(f"\n# exercício 7 e 8:\n{todos_clientes_lojas}")

    # exercício 9
    soma_gastos_clientes_loja_a = data_frame_cadastro_loja_a.merge(
        data_frame_vendas,
        how="inner",
        on="ID"
    )["Valor"].sum()

    print(f"\n# exercício 9:\n{soma_gastos_clientes_loja_a}")

    # exercício 10
    nome_tipo_cliente_vendas = data_frame_vendas.merge(
        data_frame_cadastro_loja_a.merge(
            data_frame_tipo_cliente,
            how="inner",
            left_on="TipoCliente",
            right_on="ID",
            suffixes=("_A", "_B")
        ),
        how="inner",
        left_on="ID",
        right_on="ID_A"
    ).merge(
        data_frame_cadastro_loja_b.merge(
            data_frame_tipo_cliente,
            how="inner",
            left_on="TipoCliente",
            right_on="ID",
            suffixes=("_A", "_B")
        ),
        how="outer"
    ).drop_duplicates(
        subset="ID_A"
    ).drop(
        ["ID", "Data", "TipoCliente_A", "ID_B"],
        axis=1
    ).rename(
        columns={
            "ID_A": "ID",
            "TipoCliente_B": "TipoCliente"
        }
    ).reset_index().drop(
        ["index"],
        axis=1
    )

    print(f"\n# exercício 10:\n{nome_tipo_cliente_vendas}")

    # exercício 11
    clientes_loja_a_nao_compraram = data_frame_cadastro_loja_a.merge(
        data_frame_vendas,
        how="left",
        on="ID"
    )

    clientes_loja_a_nao_compraram = clientes_loja_a_nao_compraram[
        clientes_loja_a_nao_compraram["Valor"].isnull()
    ]

    print(f"\n# exercício 11:\n{clientes_loja_a_nao_compraram}")

    # exercício 12
    clientes_loja_b_nao_compraram = data_frame_cadastro_loja_b.merge(
        data_frame_vendas,
        how="left",
        on="ID"
    )

    clientes_loja_b_nao_compraram = clientes_loja_b_nao_compraram[
        clientes_loja_b_nao_compraram["Valor"].isnull()
    ]

    print(f"\n# exercício 12:\n{clientes_loja_b_nao_compraram}")

    # exercício 13
    todos_clientes_loja_a_nao_compras = data_frame_vendas.merge(
        data_frame_cadastro_loja_a,
        how="outer",
        on="ID"
    )

    todos_clientes_loja_a_nao_compras = todos_clientes_loja_a_nao_compras[
        todos_clientes_loja_a_nao_compras["Valor"].isnull()
    ]

    todos_clientes_loja_b_nao_compras = data_frame_vendas.merge(
        data_frame_cadastro_loja_b,
        how="outer",
        on="ID"
    )

    todos_clientes_loja_b_nao_compras = todos_clientes_loja_b_nao_compras[
        todos_clientes_loja_b_nao_compras["Valor"].isnull()
    ]

    todos_clientes_lojas_nao_compras = pd.concat([
        todos_clientes_loja_a_nao_compras,
        todos_clientes_loja_b_nao_compras
    ]).drop_duplicates(
        subset="ID"
    ).drop(
        ["Data", "Valor"],
        axis=1
    )

    print(f"\n# exercício 13:\n{todos_clientes_lojas_nao_compras}")

    # exercício 14
    todos_clientes_lojas_compras = todos_clientes_lojas.merge(
        data_frame_vendas,
        how="inner",
        on="ID"
    )

    todos_clientes_lojas_compras = todos_clientes_lojas_compras[
        todos_clientes_lojas_compras["Valor"].notnull()
    ]

    print(f"\n# exercício 14:\n{todos_clientes_lojas_compras}")

    # exercício 15
    tres_mais_compraram = todos_clientes_lojas_compras.sort_values(
        ["Valor"],
        ascending=False
    )[:3]

    tres_mais_compraram = pd.DataFrame(
        tres_mais_compraram,
        columns=[
            "ID",
            "Nome_A",
            "Nome_B",
            "Valor"
        ]
    ).reset_index().drop(
        "index",
        axis=1
    )

    print(f"\n# exercício 15:\n{tres_mais_compraram}")

