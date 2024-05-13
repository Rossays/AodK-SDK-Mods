import unrealsdk
from unrealsdk import *

from ..ModMenu import SDKMod, Game, EnabledSaveType, ModTypes, Hook, RegisterMod, Options, OptionManager

oidLevelSlider = Options.Slider(
    Caption="Level Slider",
    Description="Fine adjust the levels of areas using this slider. Values are based on your level. You need to load into a new area or reload for changes to take effect.",
    StartingValue=0,
    MinValue=-15,
    MaxValue=15,
    Increment=1,
)

class Scaler(SDKMod):
    Name: str = "Game Scaler"
    Description: str = ("Scales all zones in Normal Mode and True Vault Hunter Mode to your level, and removes the level cap for TVHM scaling in BL2 and TPS.\n"
                       "In BL2 and TPS, Normal Mode level cap is 35, TVHM minimum level is 30.\n"
                       "In AoDK, Normal Mode level cap is 18 and TVHM minimum level is 17.")
    Version: str = "2.1"
    Author: str = "Rossay"
    SupportedGames = Game.BL2 | Game.TPS | Game.AoDK
    Types: ModTypes = ModTypes.Gameplay | ModTypes.Utility
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu
    Options = [oidLevelSlider]

    if Game.GetCurrent() == Game.AoDK: 
        @Hook("WillowGame.WillowPlayerController.SpawningProcessComplete")
        def onSpawn(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
            player_level = (unrealsdk.GetEngine().GamePlayers[0].Actor.GetCachedSaveGame().ExpLevel) + (oidLevelSlider.CurrentValue)
            balance_normal_mode_AoDK = unrealsdk.FindObject("GameBalanceDefinition", "GD_Aster_GameStages.Balance.Aster_P1_GameBalance")
            balance_tvhm_AoDK = unrealsdk.FindObject("GameBalanceDefinition", "GD_Aster_GameStages.Balance.Aster_P2_GameBalance")
            for region in balance_normal_mode_AoDK.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 18)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 18)
            for region in balance_tvhm_AoDK.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 17)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 17)
            return True
    elif Game.GetCurrent() == Game.BL2:
        @Hook("WillowGame.WillowPlayerController.SpawningProcessComplete")
        def onSpawn(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
            player_level = (unrealsdk.GetEngine().GamePlayers[0].Actor.GetCachedSaveGame().ExpLevel) + (oidLevelSlider.CurrentValue)
            balance_normal_mode1 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Aster_GameStages.Balance.Aster_P1_GameBalance")
            balance_tvhm1 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Aster_GameStages.Balance.Aster_P2_GameBalance")
            balance_normal_mode2 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Allium_GameStages.Balance.Allium_P1_GameBalance")
            balance_tvhm2 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Allium_GameStages.Balance.Allium_P2_GameBalance")
            balance_normal_mode3 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Anemone_GameStages.Balance.Anemone_P1_GameBalance")
            balance_tvhm3 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Anemone_GameStages.Balance.Anemone_P2_GameBalance")
            balance_normal_mode4 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Flax_GameStages.Balance.Flax_P1_GameBalance")
            balance_tvhm4 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Flax_GameStages.Balance.Flax_P2_GameBalance")
            balance_normal_mode5 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P1_Zone1")
            balance_tvhm5 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P2_Zone1")
            balance_normal_mode6 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P1_Zone1_Interlude")
            balance_tvhm6 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P2_Zone1_Interlude")
            balance_normal_mode7 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P1_Zone2")
            balance_tvhm7 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P2_Zone2")
            balance_normal_mode8 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P1_Zone3")
            balance_tvhm8 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P2_Zone3")
            balance_normal_mode9 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Iris_GameStages.Balance.Iris_P1_GameBalance")
            balance_tvhm9 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Iris_GameStages.Balance.Iris_P2_GameBalance")
            balance_normal_mode10 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Lobelia_GameStages.Balance.Lobelia_P1_GameBalance")
            balance_tvhm10 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Lobelia_GameStages.Balance.Lobelia_P2_GameBalance")
            balance_normal_mode11 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Nasturtium_GameStages.Balance.Nasturtium_P1_GameBalance")
            balance_tvhm11 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Nasturtium_GameStages.Balance.Nasturtium_P2_GameBalance")
            balance_normal_mode12 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Orchid_GameStages.Balance.Orchid_P1_GameBalance")
            balance_tvhm12 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Orchid_GameStages.Balance.Orchid_P2_GameBalance")
            balance_normal_mode13 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Sage_GameStages.Balance.Sage_P1_GameBalance")
            balance_tvhm13 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Sage_GameStages.Balance.Sage_P2_GameBalance")
            for region in balance_normal_mode1.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm1.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode2.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm2.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode3.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm3.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode4.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm4.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode5.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm5.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode6.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm6.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode7.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm7.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode8.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm8.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode9.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm9.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode10.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm10.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode11.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm11.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode12.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm12.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode13.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm13.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            return True
    elif Game.GetCurrent() == Game.TPS:
        @Hook("WillowGame.WillowPlayerController.SpawningProcessComplete")
        def onSpawn(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
            player_level = (unrealsdk.GetEngine().GamePlayers[0].Actor.GetCachedSaveGame().ExpLevel) + (oidLevelSlider.CurrentValue)
            balance_normal_mode1 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Ma_GameStages.Marigold_P1_GameBalance")
            balance_tvhm1 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Ma_GameStages.Marigold_P2_GameBalance")
            balance_normal_mode2 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Pet_GameStages.Balance.Petunia_P1_GameBalance")
            balance_tvhm2 = unrealsdk.FindObject("GameBalanceDefinition", "GD_Pet_GameStages.Balance.Petunia_P2_GameBalance")
            balance_normal_mode3 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P1_Zone4")
            balance_tvhm3 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P2_Zone4")
            balance_normal_mode4 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P1_Zone1")
            balance_tvhm4 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P2_Zone1")
            balance_normal_mode5 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P1_Zone2")
            balance_tvhm5 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P2_Zone2")
            balance_normal_mode6 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P1_Zone3")
            balance_tvhm6 = unrealsdk.FindObject("GameBalanceDefinition", "GD_GameStages.Balance.Balance_P2_Zone3")
            for region in balance_normal_mode1.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm1.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode2.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm2.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode3.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm3.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode4.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm4.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode5.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm5.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            for region in balance_normal_mode6.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = min(player_level, 35)
                region.MaxDefaultGameStage.BaseValueConstant = min(player_level, 35)
            for region in balance_tvhm6.BalanceByRegion:
                region.MinDefaultGameStage.BaseValueConstant = max(player_level, 30)
                region.MaxDefaultGameStage.BaseValueConstant = max(player_level, 30)
            return True


RegisterMod(Scaler())
