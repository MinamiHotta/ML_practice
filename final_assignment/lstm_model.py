import torch
import torch.nn as nn
import torch.nn.functional as F

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size=6): # concatしたベクトル.sizeがinput_sizeに入ってくる batch_size
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, input_ids):
        out, _ = self.lstm(input_ids)
        out = self.fc(out[:, -1])
        out = F.softmax(out, dim=1)            
        return out

class BiLSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size=6):
        super(BiLSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # Bidirectional LSTM
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size * 2, output_size) # 隠れ状態とセル状態のサイズを双方向用に2倍に

    def forward(self, input_ids):
        out, _ = self.lstm(input_ids)
        out = self.fc(out[:, -1])
        out = F.softmax(out, dim=1)            
        return out