import numpy as np
import task_2 as model_nn


for layer_1 in range(5, 16):
    for layer_2 in range(4, 11):
        for epochs in range(10, 50, 5):
            for batch_size in range(10, 50, 5):
                my_model = model_nn.Neural(layer_1, layer_2, 1, 8, epochs, batch_size, 2)
                my_model.prepare_data()
                my_model.learn_network()
                #test_batch = (np.expand_dims(my_model.X, axis=1))
                test_batch = my_model.X
                with open (f'./result/out {layer_1}-{layer_2}-{epochs}-{batch_size}.txt', "a+") as f:
                    f.write(f'Parameter: layer 1 = {layer_1}, layer_2 = {layer_2}, epochs = {epochs}, batch_size = {batch_size}\n')
                    for i in range(3):
                        f.write(f'{my_model.inference(test_batch[:5])}\n\n')



