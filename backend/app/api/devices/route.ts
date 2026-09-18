import { NextResponse } from "next/server";
import { supabase } from "@/lib/supabase/client";

// GET /api/devices
export async function GET() {
  const { data, error } = await supabase
    .from("devices")
    .select("*")
    .order("created_at", { ascending: false });

if (error) {
  console.error("SUPABASE INSERT ERROR:", error);

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

  return NextResponse.json({
    success: true,
    data,
  });
}

// POST /api/devices
export async function POST(request: Request) {
  try {
    const body = await request.json();

    console.log("REQUEST BODY:", body);

    const { data, error } = await supabase
      .from("devices")
      .insert({
        device_id: body.device_id,
        name: body.name ?? null,
        device_type: body.device_type,
        location: body.location ?? null,
      })
      .select()
      .single();

    console.log("SUPABASE DATA:", data);
    console.log("SUPABASE ERROR:", error);

    if (error) {
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
    console.error("REQUEST ERROR:", error);

    return NextResponse.json(
      {
        success: false,
        error: String(error),
      },
      { status: 400 }
    );
  }
}