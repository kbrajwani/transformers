# coding=utf-8
# Copyright (c) Facebook, Inc. and its affiliates.
# Copyright (c) HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" MMBT configuration """


from . import hf_logging


logger = hf_logging.get_logger(__name__)


class MMBTConfig(object):
    """Configuration class to store the configuration of a `MMBT Model`.

    Args:
        config (:obj:`~transformers.PreTrainedConfig`):
            Config of the underlying Transformer models. Its values are
            copied over to use a single config.
        num_labels (:obj:`int` or :obj:`None`, optional, defaults to `None`):
            Size of final Linear layer for classification.
        modal_hidden_size (:obj:`int`, optional, defautls to 2048):
            Embedding dimension of the non-text modality encoder.
    """

    def __init__(self, config, num_labels=None, modal_hidden_size=2048):
        self.__dict__ = config.__dict__
        self.modal_hidden_size = modal_hidden_size
        if num_labels:
            self.num_labels = num_labels
