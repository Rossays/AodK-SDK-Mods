import unrealsdk
from unrealsdk import *

from ..ModMenu import SDKMod, Game, EnabledSaveType, ModTypes, Hook, RegisterMod


class Scaler(SDKMod):
    Name = "Normal Mode Scaler"
    Description = "Scales all zones in Normal Mode to your level, with a level cap of 17."
    Version = "1.0"
    SupportedGames = Game.AoDK
    Types = ModTypes.Utility | ModTypes.Gameplay
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu
    Author = "Rossay"

    @Hook("WillowGame.WillowPlayerController.SpawningProcessComplete")
    def onSpawn(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
        player_level = unrealsdk.GetEngine().GamePlayers[0].Actor.GetCachedSaveGame().ExpLevel
        balance_normal_mode = unrealsdk.FindObject("GameBalanceDefinition", "GD_Aster_GameStages.Balance.Aster_P1_GameBalance")
        for region in balance_normal_mode.BalanceByRegion:
            region.MinDefaultGameStage.BaseValueConstant = min(player_level, 17)
            region.MaxDefaultGameStage.BaseValueConstant = 17
        return True


RegisterMod(Scaler())
