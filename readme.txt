・環境構築
配下のファイル、フォルダを全部ダウンロードした後、
コマンドプロンプトで、ダウンロードしたフォルダに移動後、
「docker compose up」コマンドでKongが構築できます。

※1 kong-migration-1のサービスは、kong-gatewayとpostgresSQLを接続させるためのものです。
    コネクションが確立できたら、終了されます。

※2 kong-gateway起動時に、「connect() to unix:/usr/local/kong/python_pluginserver.sock failed (2: No such file or directory)」が複数回表示されますが、
    Python plugin用のサーバー起動準備中に出力されるものです。何回か出力された後、でなくなれば、pluginの準備ができた状態になります。

・pluginについて
 kong-py-pluginsにPythonのソースを格納した後、dockercompose.ymlの「KONG_PLUGINS: 」にそのpluginのファイル名(拡張子なし)を
 追記して、kong-gatewayの再起動をしてください。「bundled」は必須なので、消さないでください。

・kongの操作
curlコマンドでapiによる操作も可能ですが、画面での操作もできます。
画面は、「http://localhost:8002/overview」で入ってください。


※ Kongの詳細については、「https://docs.konghq.com/gateway/latest/install/docker/」を参照してください。