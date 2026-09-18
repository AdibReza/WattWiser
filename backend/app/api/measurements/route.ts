import { NextResponse } from "next/server";
import { supabase } from "@/lib/supabase/client";

// GET /api/measurements
export async function GET() {
  const { data, error } = await supabase
    .from("measurements")
    .select("*")
    .order("timestamp", { ascending: false })
    .limit(100);

  if (error) {
    return NextResponse.json(
      {
        success: false,
        error: error.message,
      },
      { status: 500 }
    );
  }

  return NextResponse.json({
    success: true,
    data,
  });
}

// POST /api/measurements
export async function POST(request: Request) {
  try {
    const body = await request.json();

    const {
      device_id,
      timestamp,
      voltage_v,
      current_a,
      active_power_w,
      apparent_power_va,
      power_factor,
      frequency_hz,
      energy_wh,
    } = body;

    if (!device_id || !timestamp) {
      return NextResponse.json(
        {
          success: false,
          error: "device_id and timestamp are required",
        },
        { status: 400 }
      );
    }

    const { data, error } = await supabase
      .from("measurements")
      .insert({
        device_id,
        timestamp,
        voltage_v: voltage_v ?? null,
        current_a: current_a ?? null,
        active_power_w: active_power_w ?? null,
        apparent_power_va: apparent_power_va ?? null,
        power_factor: power_factor ?? null,
        frequency_hz: frequency_hz ?? null,
        energy_wh: energy_wh ?? null,
      })
      .select()
      .single();

    if (error) {
      console.error("SUPABASE MEASUREMENT ERROR:", error);

      return NextResponse.json(
        {
          success: false,
          error: error.message,
          details: error.details,
          hint: error.hint,
          code: error.code,
        },
        { status: 500 }
      );
    }

    return NextResponse.json(
      {
        success: true,
        data,
      },
      { status: 201 }
    );
  } catch (error) {
    console.error("MEASUREMENT REQUEST ERROR:", error);

    return NextResponse.json(
      {
        success: false,
        error: "Invalid request body",
      },
      { status: 400 }
    );
  }
}