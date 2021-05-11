import pandas


if __name__ == '__main__':
    filename = "./Datasets/Imóveis.csv"

    frame = pandas.read_csv(filename, sep=",")

    print(f"\n{frame.shape}")

    print(f"\n{frame.head(10)}")

    print(f"\n{frame.columns}")

    print(f"\n{frame.dtypes}")

    frame["data"] = pandas.to_datetime(frame["data"])

    frame["análise"] = 2021

    print(f"\n{pandas.DataFrame(frame, columns=['id', 'data', 'preço', 'quartos', 'banheiros', 'ano de construção'])}")

    frame.drop(["metragem da casa.1"], axis=1)  # axis começa em 0, main axis = linha

    frame["banheiros"] = frame["banheiros"].apply(lambda num: str(num).split(",")[0]).astype('int64')

    print(f"\n{frame.loc[frame['ano de construção'] < 2000]}")

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

    frame["DS_TIPO_CONDICAO"] = ["Ruim" if num < 2 else "Regular" if num <= 4 else "Bom" for num in frame["condição"]]

    print(f"\n{frame['DS_TIPO_CONDICAO']}")

    frame["VL_PRECO"] = frame["VL_PRECO"].apply(lambda num: str(num).replace(",", ".")).astype('float64')

    print(f"\n{frame[['id', 'VL_PRECO']].sort_values(['VL_PRECO'])}")

    frame_filtro_1 = frame.query("DS_TIPO_CONDICAO == 'Regular'")

    print(f"\n{frame_filtro_1.shape[0]}")

    print(f"\n{frame_filtro_1['VL_PRECO'].mean()}")

    frame_filtro_2 = frame.query("QTD_QUARTOS == 3")

    preco_max = frame_filtro_2['VL_PRECO'].max()

    print(f"\n{preco_max}")

    frame_filtro_3 = frame.query("DS_TIPO_CONDICAO == 'Bom' and QTD_QUARTOS > 2 and QTD_BANHEIROS > 2")

    print(f"\n{frame_filtro_3}")

    preco_max = frame['VL_PRECO'].max()

    frame_casa_maior_preco = frame[frame['VL_PRECO'] == preco_max]

    print(f"\n{frame_casa_maior_preco['id']}")

    preco_min = frame['VL_PRECO'].min()

    frame_casa_menor_preco = frame[frame['VL_PRECO'] == preco_min]

    print(f"\n{frame_casa_menor_preco['id']}")

    print(f"\n{frame['DT_REFERENCIA'].min()}")

    print(f"\n{frame.groupby(['DS_TIPO_CONDICAO']).size().reset_index(name='QTD_IMOVEIS')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['VL_PRECO'].mean().reset_index(name='VL_MEDIA')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['QTD_QUARTOS'].min().reset_index(name='NU_MENOR_QUARTOS')}")

    print(f"\n{frame.groupby(['QTD_QUARTOS', 'QTD_BANHEIROS'])['VL_PRECO'].sum().reset_index(name='VL_SOMATORIO')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['VL_PRECO'].median().reset_index(name='VL_MEDIANA')}")

    frame["NU_CLASSIFICACAO_PRECO_1"] = [0 if num < 321950 else 1 if num <= 450000 else 2 if num <= 645000 else 3 for num in frame["VL_PRECO"]]

    print(f"\n{frame.head()}")

    frame["NU_CLASSIFICACAO_PRECO_2"] = frame["VL_PRECO"].apply(lambda num: 0 if num < 321950 else 1 if num <= 450000 else 2 if num <= 645000 else 3)

    print(f"\n{frame.head()}")

    media_preco = pandas.DataFrame({
        "id": [x for x, y in enumerate(frame.groupby(["NU_CEP"]))],
        "VL_MEDIA_PRECO": frame.groupby(["NU_CEP"])["VL_PRECO"].mean()
    }).reset_index()

    print(f"{media_preco}")

    media_preco.to_csv("./Datasets/Imóveis2.csv", index=False)
