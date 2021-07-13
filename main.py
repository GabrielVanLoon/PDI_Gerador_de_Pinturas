#!/usr/bin/env python3
import imageio
import numpy as np
from skimage.segmentation import slic
from skimage.measure import regionprops
from scipy.ndimage import gaussian_filter

from src.utils import load_image, image_downsampling
from src.quantization import palette_kmeans
from src.segmentation import labels_to_edges_thin

def main():
    print(" _                      ___          _                   ")
    print("|_) o __ _|_    __ _     |  _  __ _ |_) _    _|_ o  _  _ ")
    print("|   | | | |_|_| | (_|    | (/_ | (_||  (/_|_| |_ | (_ (_|")
    print("~~~~~~~~~~~~~~~~~~~~~   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    # Image loading and reading parameters
    try:
        print("[ ] 0º Step - Iniciando parâmetros...")
        image_path  = input("[+]   Caminho da imagem a ser convertida: ").rstrip()
        output_name = input("[+]   Nome da imagem de output: ").rstrip()
        N           = int(input("[+]   Quantidade de tintas na paleta: "))
        use_slic    = input("[+]   Usar SLIC Segmentation? (y/n): ").strip()[0] in ["y", "s", "Y", "S"]
        
        if use_slic:
            slic_comp          = int(input("[+]   SLIC Parametros - Compacidade: "))
            slic_n_segments    = int(input("[+]   SLIC Parametros - Qtd. de segmentos: "))
    except:
        print("[x] Erro: verifique se os parâmetros foram inseridos corretamente!")
        exit(0)

    # Image Loading
    try:
        print(f"[ ] 1º Step - Carregando a imagem em {image_path}...")
        image = load_image(image_path)[:,:,:3]
    except:
        print("[x] Erro: verifique se o caminho da imagem foi inserido corretamente!")
        exit(0)

    # Image pre-proccessing
    try:
        print(f"[ ] 2º Step - Pré-processando a imagem...")
        image = image_downsampling(image)
        image_smooth = np.zeros(image.shape)
        for c in range(3):
            image_smooth[:,:,c] = gaussian_filter(image[:,:,c], sigma=2, mode='nearest')
    except:
        print("[x] Erro: ocorreu um erro durante o pré-processamento :(")
        exit(0)
    
    # Palette extraction
    try:
        print("[ ] 3º Step - Extração de paleta de cores com Kmeans...")
        print("[+]   Obs: a execução pode levar até 2 minutos")
        palette, image_recolorized, predicted_labels, model = palette_kmeans(image_smooth, N)
    except:
        print("[x] Erro: ocorreu um erro durante a extração das cores :(")
        exit(0)

    # If SLIC not used, can skip this part
    if use_slic:
        try:
            print("[ ] 4º Step - Iniciando segmentação SLIC...")
            slic_segments = slic(image_smooth, n_segments=slic_n_segments*slic_n_segments, compactness=slic_comp, max_iter=50, convert2lab=False, start_label=0)
            segments_properties = regionprops(slic_segments, intensity_image=image_smooth)
            print("[+]   Quantidade de labels geradas: ", np.max(slic_segments)+1)
        except:
            print("[x] Erro: ocorreu um erro durante a segmentação slic :(")
            exit(0)

        try:
            print("[ ] 5º Step - Calculando intensidade média dos segmentos...")
            mean_intensities = np.array([segments_properties[l].mean_intensity for l in range(0, len(segments_properties))])
        except:
            print("[x] Erro: erro durante cálculo das intensidades :(")
            exit(0)

        try:
            print("[ ] 6º Step - Recolorindo segmentos da imagem...")
            slic_recolorized = np.empty_like(image_smooth)

            for i in range(image_smooth.shape[0]):
                for j in range(image_smooth.shape[1]):
                    slic_recolorized[i,j,:] = mean_intensities[slic_segments[i,j]-1]
        except:
            print("[x] Erro: ocorreu um erro durante recolorização da imagem :(")
            exit(0)

        try:
            print("[ ] 7º Step - Ajustando segmentos SLIC para a paleta de cores...")
            predicted_labels = model.predict(slic_recolorized.reshape(-1,3)).reshape((image_smooth.shape[0],image_smooth.shape[1]))
            image_recolorized = np.empty_like(image_smooth)

            for i in range(image_smooth.shape[0]):
                for j in range(image_smooth.shape[1]):
                    image_recolorized[i,j,:] = palette[predicted_labels[i,j]]
        except:
            print("[x] Erro: ocorreu um erro durante a extração das cores :(")
            exit(0)

    # Generate output images
    try:
        print("[ ] Final Step - Gerando a imagem colorível e seu preview...")
        edgesmap = labels_to_edges_thin(predicted_labels)
        imageio.imwrite(f"./images/output/{output_name}_recolorized.jpg", image_recolorized.astype(np.uint8))
        imageio.imwrite(f"./images/output/{output_name}_edges_slic.jpg", edgesmap.astype(np.uint8) * 255)
    except:
        print("[x] Erro: ocorreu um erro durante a criação das imagens :(")
        exit(0)

    print(f"[ ] Imagens geradas com sucesso em ./images/output/{output_name}_* :D")


if __name__ == "__main__":
    main()
