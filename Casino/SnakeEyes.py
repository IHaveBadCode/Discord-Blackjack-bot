import random, discord, Methods, BankMethods

async def Start(bot, ctx, bet):
  def DiceConv(dice):
    Code={
     1:"\u2680",
     2:"\u2681",
     3:"\u2682",
     4:"\u2683",
     5:"\u2684",
     6:"\u2685"}
    return f"{Code[dice[0]]}{Code[dice[1]]}"

  BankMethods.update_wallet(ctx,-abs(bet))
  Dice=[random.randint(1,6), random.randint(1,6)]
  embed = Methods.Embeds(bot, ctx)
  embed.Create()
  embed.DisplayNameSet(f"{ctx.author.name}'s Snake Eyes game")
  embed.ColorSet(discord.Color.from_rgb(43, 243, 28))
  num=Dice.count(1)
  if num == 2:
    embed.FieldAdd(f"{DiceConv(Dice)}",
                   f"SNAKE EYES! You won 10x your bet:{bet*10}\nNow you have {BankMethods.get_wallet(ctx)+bet*10}")
    BankMethods.update_wallet(ctx,+abs(bet*10))
  if num == 1:
    embed.FieldAdd(f"{DiceConv(Dice)}",
                   f"A single eye, not bad. you won 1.5X your bet:{bet*1.5}\nNow you have{BankMethods.get_wallet(ctx)+bet*1.5}")
    BankMethods.update_wallet(ctx,+abs(bet*1.5))
  
  if num == 0:
    embed.FieldAdd(f"{DiceConv(Dice)}",
                   f"You didn't get any snake eyes. Sadge. Youlost your bet.\nNow you have{BankMethods.get_wallet(ctx)-bet}")
  
  await embed.Send()
  