�E���\�z
�z���̃t�@�C���A�t�H���_��S���_�E�����[�h������A
�R�}���h�v�����v�g�ŁA�_�E�����[�h�����t�H���_�Ɉړ���A
�udocker compose up�v�R�}���h��Kong���\�z�ł��܂��B

��1 kong-migration-1�̃T�[�r�X�́Akong-gateway��postgresSQL��ڑ������邽�߂̂��̂ł��B
    �R�l�N�V�������m���ł�����A�I������܂��B

��2 kong-gateway�N�����ɁA�uconnect() to unix:/usr/local/kong/python_pluginserver.sock failed (2: No such file or directory)�v��������\������܂����A
    Python plugin�p�̃T�[�o�[�N���������ɏo�͂������̂ł��B���񂩏o�͂��ꂽ��A�łȂ��Ȃ�΁Aplugin�̏������ł�����ԂɂȂ�܂��B

�Eplugin�ɂ���
 kong-py-plugins��Python�̃\�[�X���i�[������Adockercompose.yml�́uKONG_PLUGINS: �v�ɂ���plugin�̃t�@�C����(�g���q�Ȃ�)��
 �ǋL���āAkong-gateway�̍ċN�������Ă��������B�ubundled�v�͕K�{�Ȃ̂ŁA�����Ȃ��ł��������B

�Ekong�̑���
curl�R�}���h��api�ɂ�鑀����\�ł����A��ʂł̑�����ł��܂��B
��ʂ́A�uhttp://localhost:8002/overview�v�œ����Ă��������B


�� Kong�̏ڍׂɂ��ẮA�uhttps://docs.konghq.com/gateway/latest/install/docker/�v���Q�Ƃ��Ă��������B