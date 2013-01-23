defmodule Hello do
  IO.puts "Defining the function world"
  def world do
    IO.puts "Hello World"
    :application.start(:crypto)
	i = :crypto.md5("Using crypto from yes Erlang OTP")
	IO.puts i
  end
  IO.puts "Function world defined"
end

Hello.world