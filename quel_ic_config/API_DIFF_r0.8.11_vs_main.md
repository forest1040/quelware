# quel_ic_config API差分まとめ（r0.8.11 ↔ main）

対象: r0.8.11 ブランチ配下の v0.8.11/quel_ic_config と、main の quel_ic_config

- r0.8.11 側: [v0.8.11/quel_ic_config](v0.8.11/quel_ic_config)
- main 側: [quel_ic_config](quel_ic_config)

## 概要
- AD9082 バックエンドが v106 から v170 へ移行し、公開APIの名称・エクスポートが整理されました。
- 旧 `GenericGpio` 系や `e7workaround` 系のAPIが整理・廃止され、ロック/アンロック系のユーティリティ、E7リソースマッパーの抽象化が追加されました。
- 温度センサ/サーミスタのAPIは `thermistor.py` から `quel1_thermistor.py` へ整理され、`Quel1Thermistor` 型が導入されています。
- 波形サブシステムの公開APIは、旧 `Capture*` 系から、起動タスク指向 (`StartAwgunits*Task`) へリファクタされました。

## モジュール構成の差分（トップレベル .py）
- 追加（main にのみ存在）
  - [quel_ic_config/src/quel_ic_config/ad9082.py](quel_ic_config/src/quel_ic_config/ad9082.py) （旧 `ad9082_v106.py` の刷新。バックエンド v170 対応）
  - [quel_ic_config/src/quel_ic_config/box_force_unlock.py](quel_ic_config/src/quel_ic_config/box_force_unlock.py)
  - [quel_ic_config/src/quel_ic_config/box_lock.py](quel_ic_config/src/quel_ic_config/box_lock.py)
  - [quel_ic_config/src/quel_ic_config/quel1_thermistor.py](quel_ic_config/src/quel_ic_config/quel1_thermistor.py)
  - [quel_ic_config/src/quel_ic_config/quel_clock_master_v1.py](quel_ic_config/src/quel_ic_config/quel_clock_master_v1.py)
- 削除（r0.8.11 にのみ存在）
  - [v0.8.11/quel_ic_config/src/quel_ic_config/ad9082_v106.py](v0.8.11/quel_ic_config/src/quel_ic_config/ad9082_v106.py)
  - [v0.8.11/quel_ic_config/src/quel_ic_config/e7workaround.py](v0.8.11/quel_ic_config/src/quel_ic_config/e7workaround.py)
  - [v0.8.11/quel_ic_config/src/quel_ic_config/generic_gpio.py](v0.8.11/quel_ic_config/src/quel_ic_config/generic_gpio.py)
  - [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box_with_raw_wss.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box_with_raw_wss.py)
  - [v0.8.11/quel_ic_config/src/quel_ic_config/thermistor.py](v0.8.11/quel_ic_config/src/quel_ic_config/thermistor.py)

## パッケージ公開シンボル（__all__）の差分
出典: [quel_ic_config/src/quel_ic_config/__init__.py](quel_ic_config/src/quel_ic_config/__init__.py) と [v0.8.11/quel_ic_config/src/quel_ic_config/__init__.py](v0.8.11/quel_ic_config/src/quel_ic_config/__init__.py)

- 追加（main で新規にエクスポート）
  - `AbstractQuel1E7ResourceMapper`, `Quel1ConventionalE7ResourceMapper`
  - `Ad9082Generic`, `Ad9082Quel1`, `Ad9082Quel1se`
  - `AwgParam`, `CapIqDataReader`, `CapParam`, `CapSection`, `WaveChunk`
  - `BoxLockError`, `set_trancated_traceback_for_lock_error`, `force_unlock_all_boxes`
  - `LinkStatus`
  - `Quel1Thermistor`, `Quel1seAnyConfigSubsystem`, `QuelClockMasterV1`, `Quel2ProtoAddaConfigSubsystem`
  - `AbstractStartAwgunitsTask`, `StartAwgunitsNowTask`, `StartAwgunitsTimedTask`, `StartCapunitsNowTask`, `StartCapunitsByTriggerTask`
  - `ExstickgeCoapClientQuel1seRiken8WithLock`, `ExstickgeSockClientQuel1WithDummyLock`, `parse_port_str`
- 削除（r0.8.11 のみエクスポート）
  - `Ad9082V106`
  - `GenericGpio`, `GenericGpioConfigHelper`, `GenericGpioRegs`, `GenericGpioRegNames`
  - `Quel1BoxWithRawWss`
  - `CaptureModule`, `CaptureUnit`, `CaptureResults`, `CaptureReturnCode`
  - `Quel1E7ResourceMapper`, `E7LibBranch`, `detect_branch_of_library`, `resolve_hw_type`
  - `ExstickgeCoapClientQuel1seRiken8Dev1`, `ExstickgeCoapClientQuel1seRiken8Dev2`, `ExstickgeSockClientQuel1`

補足:
- `__version__` は main 側で `"0.10.7"` と固定化。r0.8.11 側は `importlib.metadata.version("quel_ic_config")` でメタデータから取得。

## 主なリネーム/置き換えポイント（移行ガイド）
- AD9082 系
  - `Ad9082V106` → `Ad9082Generic` へ置き換え。
  - さらに用途別に `Ad9082Quel1`, `Ad9082Quel1se` がパブリックエクスポートに追加。
  - バックエンドが `adi_ad9082_v106` → `adi_ad9082_v170` に更新。NCO/Jesd 等のパラメータ型は `ad9082.py` に集約。
- GPIO/汎用
  - `GenericGpio*` 一式はエクスポートから削除。
- E7 リソースマッピング
  - 旧 `Quel1E7ResourceMapper` は抽象化され、`AbstractQuel1E7ResourceMapper` と `Quel1ConventionalE7ResourceMapper` に分離。
  - 実体選択は [quel_ic_config/src/quel_ic_config/e7resource_mapper.py](quel_ic_config/src/quel_ic_config/e7resource_mapper.py) の `create_rmap_object()` でFW種別に応じて生成（パブリックエクスポートではないが、利用形態が変更）。
- サーミスタ/温度系
  - `thermistor.py` → `quel1_thermistor.py`。`Quel1Thermistor` ベースで `Quel1NormalThermistor`, `Quel1PathSelectorThermistor`, `Quel1seOnboardThermistor`, `Quel1seExternalThermistor` をエクスポート。
- 波形/キャプチャ系
  - 旧 `CaptureResults` `CaptureReturnCode` 中心の公開APIから、起動タスク中心 (`AbstractStartAwgunitsTask`, `StartAwgunitsNowTask`, `StartAwgunitsTimedTask`, `StartCapunits*Task`) に整理。
- ボックスロック
  - 新規に `BoxLockError`, `set_trancated_traceback_for_lock_error`, `force_unlock_all_boxes` を公開。
- クロックマスター
  - `QuelClockMasterV1` が公開追加。

## 互換性影響のまとめ
- 名前変更/削除により、インポートの修正が必要な箇所が発生します。
  - 例: `from quel_ic_config import Ad9082V106` → `from quel_ic_config import Ad9082Generic`
  - 例: `from quel_ic_config import GenericGpio` → 代替無し（用途に応じた個別GPIOモジュールへ移行検討）
  - 例: `from quel_ic_config import Quel1E7ResourceMapper` → `from quel_ic_config import AbstractQuel1E7ResourceMapper, Quel1ConventionalE7ResourceMapper`（実体生成は `create_rmap_object()` 使用を検討）
  - 例: `from quel_ic_config import CaptureResults, CaptureReturnCode` → 起動タスク系APIへ移行（`StartAwgunits*Task` / `StartCapunits*Task`）
- AD9082 バックエンド更新に伴い、NCO/JESD 等のパラメータクラス利用側で引数名や型の微調整が必要な可能性があります。

## 参考リンク
- 旧版 API 一覧: [v0.8.11/quel_ic_config/src/quel_ic_config/__init__.py](v0.8.11/quel_ic_config/src/quel_ic_config/__init__.py)
- 現行 API 一覧: [quel_ic_config/src/quel_ic_config/__init__.py](quel_ic_config/src/quel_ic_config/__init__.py)
- AD9082 実装: 旧 [v0.8.11/quel_ic_config/src/quel_ic_config/ad9082_v106.py](v0.8.11/quel_ic_config/src/quel_ic_config/ad9082_v106.py) / 新 [quel_ic_config/src/quel_ic_config/ad9082.py](quel_ic_config/src/quel_ic_config/ad9082.py)
- E7 リソースマッパ: 旧 [v0.8.11/quel_ic_config/src/quel_ic_config/e7resource_mapper.py](v0.8.11/quel_ic_config/src/quel_ic_config/e7resource_mapper.py) / 新 [quel_ic_config/src/quel_ic_config/e7resource_mapper.py](quel_ic_config/src/quel_ic_config/e7resource_mapper.py)

---
本ファイルは自動抽出（トップレベルファイル差分と `__all__` 差分）に基づくサマリです。更に詳細なメソッドシグネチャ差分が必要であればお知らせください。

## 詳細差分（モジュール別）

より網羅的なモジュール別の公開API差分は、次の詳細ドキュメントをご参照ください。

- 詳細版: [quel_ic_config/API_DIFF_details.md](quel_ic_config/API_DIFF_details.md)