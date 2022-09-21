def load_weidgts_to_model(name_nodel, index_path, weights_path, model):
    """
    Функция подгрузки весов в модель в Colab по внешним ссылкам Google Disk
    :param name_nodel: имя модели в папке GD
    :param index_path: путь к файлу индексов
    :param weights_path: путь к файлу весов
    :param model: модель Keras в которую сохраняем веса
    """
    import gdown
    head_https = 'https://drive.google.com/uc?id='
    # находим ID
    file_id = index_path.split('/')[-2]
    weights_index = name_nodel + '.index'
    # Подгружаем на диск ноута сами веса и файл индексации
    gdown.download(head_https + file_id,
                   weights_index, quiet=False)
    # находим ID
    file_id = weights_path.split('/')[-2]
    weights = name_nodel + '.data-00000-of-00001'
    gdown.download(head_https + file_id,
                   weights, quiet=False)
    # загружаем веса в сформированный корпус модели
    path_weights = '/content/' + name_nodel
    model.load_weights(path_weights)
